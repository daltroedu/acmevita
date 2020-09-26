from flask import request
from flask_restx import Namespace, Resource, abort
from app.extensions.database import db
from app.blueprints.common.pagination import paginate
from app.blueprints.business.v1.departament.models import Departament
from app.blueprints.business.v1.departament.schemas import departament_schema, departaments_schema
from app.blueprints.business.v1.employee.models import Employee
from app.blueprints.business.v1.employee.schemas import employees_schema

api = Namespace('departaments', description='')

from .swagger import departament_model


@api.route('/')
class DepartamentList(Resource):
    def get(self):
        """Get all departaments"""

        departament = Departament.query.all()
        result = departaments_schema.dump(departament)
        data = paginate(
            query=Departament.query,
            result=result,
            page=request.args.get('page', 1, type=int),
            per_page=min(request.args.get('per_page', 10, type=int), 100),
            endpoint='bp_v1.departaments_departament_list'
        )
        return data, 200

    @api.doc(body=departament_model, responses={201:'Success'})
    def post(self):
        """Create a departament"""

        data = request.get_json() or {}
        if Departament.query.filter_by(name=data['name']).first():
            abort(409, 'please use a different departament name')
        departament = Departament(data)
        db.session.add(departament)
        db.session.commit()
        response = departament_schema.dump(departament)
        return response, 201


@api.route('/<string:id>')
@api.doc(params={'id': 'Departament UUID'})
class DepartamentResource(Resource):
    def get(self, id):
        """Get a departament"""

        departament = Departament.query.get_or_404(id)
        result = departament_schema.dump(departament)
        return result, 200

    @api.doc(body=departament_model)
    def put(self, id):
        """Update a departament"""

        departament = Departament.query.get_or_404(id)
        data = request.get_json() or {}
        instance = departament_schema.load(data, instance=departament, partial=True)
        db.session.add(instance)
        db.session.commit()
        result = departament_schema.dump(instance)
        return result, 200

    @api.doc(responses={204: 'Success'})
    def delete(self, id):
        """Delete a departament"""

        departament = Departament.query.get_or_404(id)
        db.session.delete(departament)
        db.session.commit()
        return '', 204


@api.route('/employees')
class DepartamentEmployeeList(Resource):
    def get(self):
        """Get all departments and list all employees by departments"""

        departament = Departament.query.all()
        result = departaments_schema.dump(departament)

        for i, departament in enumerate(result):
            employee = Employee.query.join(Departament).\
                        filter(Employee.departament_id == departament['id']).all()
            employee_schema = employees_schema.dump(employee)
            employees_departament = []
            for employee_data in employee_schema:
                data_aux = {
                    'id': employee_data['id'],
                    'full_name': employee_data['full_name'],
                    'have_dependents': employee_data['have_dependents']
                }
                employees_departament.append(data_aux)
            result[i]['employees'] = employees_departament

        data = paginate(
            query=Departament.query,
            result=result,
            page=request.args.get('page', 1, type=int),
            per_page=min(request.args.get('per_page', 10, type=int), 100),
            endpoint='bp_v1.departaments_departament_list'
        )
        return data, 200


@api.route('/<string:id>/employees')
@api.doc(params={'id': 'Departament UUID'})
class DepartamentEmployeeResource(Resource):
    def get(self, id):
        """Get a department and list all employees by this department"""

        if not Departament.query.filter_by(id=id).first():
            abort(404, 'departament not found')
        departament = Departament.query.get_or_404(id)
        result = departament_schema.dump(departament)

        employee = Employee.query.join(Departament).\
                    filter(Departament.id == id).\
                    filter(Employee.departament_id == id).all()
        employee_schema = employees_schema.dump(employee)
        employees_departament = []
        for employee_data in employee_schema:
            data_aux = {
                'id': employee_data['id'],
                'full_name': employee_data['full_name'],
                'have_dependents': employee_data['have_dependents']
            }
            employees_departament.append(data_aux)
        result['employees'] = employees_departament

        return result, 200