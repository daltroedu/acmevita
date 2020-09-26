from flask import request
from flask_restx import Namespace, Resource, abort
from sqlalchemy import func
from app.extensions.database import db
from app.blueprints.common.pagination import paginate
from app.blueprints.business.v1.employee.models import Employee
from app.blueprints.business.v1.employee.schemas import employee_schema, employees_schema
from app.blueprints.business.v1.dependent.models import Dependent
from app.blueprints.business.v1.dependent.schemas import dependent_schema, dependents_schema

api = Namespace('employees', description='')

from .swagger import employee_post_model, employee_put_model, dependent_model


@api.route('/')
class EmployeeList(Resource):
    def get(self):
        employee = Employee.query.all()
        result = employees_schema.dump(employee)
        data = paginate(
            query=Employee.query,
            result=result,
            page=request.args.get('page', 1, type=int),
            per_page=min(request.args.get('per_page', 10, type=int), 100),
            endpoint='bp_v1.employees_employee_list'
        )
        return data, 200

    @api.doc(body=employee_post_model, responses={201: 'Success'})
    def post(self):
        data = request.get_json() or {}
        data['have_dependents'] = False
        employee = Employee(data)
        db.session.add(employee)
        db.session.commit()

        if 'dependents' in data and data['dependents']:
            employee.dependent = []
            for full_name in data['dependents']:
                data_aux = {
                    'full_name': full_name,
                    'employee_id': employee.id
                }
                dependent = Dependent(data_aux)
                employee.dependent.append(dependent)
            employee.have_dependents = True
            db.session.add(employee)
            db.session.commit()

        response = employee_schema.dump(employee)
        return response, 201


@api.route('/<string:id>')
@api.doc(params={'id': 'Employee UUID'})
class EmployeeResource(Resource):
    def get(self, id):
        employee = Employee.query.get_or_404(id)
        result = employee_schema.dump(employee)
        return result, 200

    @api.doc(body=employee_put_model)
    def put(self, id):
        employee = Employee.query.get_or_404(id)
        data = request.get_json() or {}
        instance = employee_schema.load(data, instance=employee, partial=True)
        db.session.add(instance)
        db.session.commit()
        result = employee_schema.dump(instance)
        return result, 200

    @api.doc(responses={204: 'Success'})
    def delete(self, id):
        employee = Employee.query.get_or_404(id)
        db.session.delete(employee)
        db.session.commit()
        return '', 204


@api.route('/<string:id>/dependents')
@api.doc(params={'id': 'Employee UUID'})
class EmployeeDependentList(Resource):
    def get(self, id):
        if not Employee.query.filter_by(id=id).first():
            abort(404, 'employee not found')
        dependent = Dependent.query.filter_by(employee_id=id).all()
        result = dependents_schema.dump(dependent)
        data = paginate(
            query=Dependent.query,
            result=result,
            page=request.args.get('page', 1, type=int),
            per_page=min(request.args.get('per_page', 10, type=int), 100),
            endpoint='bp_v1.employees_employee_dependent_list',
            id=id
        )
        return data, 200

    @api.doc(body=dependent_model)
    def post(self, id):
        if not Employee.query.filter_by(id=id).first():
            abort(404, 'employee not found')
        data = request.get_json() or {}
        data['employee_id'] = id
        dependent = Dependent(data)
        db.session.add(dependent)
        db.session.commit()

        employee = Employee.query.get_or_404(id)
        if not employee.have_dependents:
            employee.have_dependents = True
            db.session.add(employee)
            db.session.commit()

        response = dependent_schema.dump(dependent)
        return response, 201


@api.route('/<string:employee_id>/dependents/<string:dependent_id>')
@api.doc(params={'employee_id': 'Employee UUID', 'dependent_id': 'Dependent UUID'})
class EmployeeDependentResource(Resource):
    def get(self, employee_id, dependent_id):
        if not Employee.query.filter_by(id=employee_id).first():
            abort(404, 'employee not found')
        if not Dependent.query.filter_by(id=dependent_id, employee_id=employee_id).first():
            abort(404, 'dependent of employee not found')
        dependent = Dependent.query.get_or_404(dependent_id)
        result = employee_schema.dump(dependent)
        return result, 200

    @api.doc(body=dependent_model)
    def put(self, employee_id, dependent_id):
        if not Employee.query.filter_by(id=employee_id).first():
            abort(404, 'employee not found')
        if not Dependent.query.filter_by(id=dependent_id, employee_id=employee_id).first():
            abort(404, 'dependent of employee not found')
        dependent = Dependent.query.get_or_404(dependent_id)
        data = request.get_json() or {}
        instance = dependent_schema.load(data, instance=dependent, partial=True)
        db.session.add(instance)
        db.session.commit()
        result = dependent_schema.dump(instance)
        return result, 200

    @api.doc(responses={204: 'Success'})
    def delete(self, employee_id, dependent_id):
        if not Employee.query.filter_by(id=employee_id).first():
            abort(404, 'employee not found')
        if not Dependent.query.filter_by(id=dependent_id, employee_id=employee_id).first():
            abort(404, 'dependent of employee not found')
        dependent = Dependent.query.get_or_404(dependent_id)
        db.session.delete(dependent)
        db.session.commit()

        count_employee_dependents = Dependent.query.filter_by(employee_id=employee_id).\
                                    with_entities(func.count(Dependent.employee_id)).scalar()
        if count_employee_dependents == 0:
            employee = Employee.query.get_or_404(employee_id)
            if employee.have_dependents:
                employee.have_dependents = False
                db.session.add(employee)
                db.session.commit()

        return '', 204