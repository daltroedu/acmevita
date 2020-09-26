from flask import request
from flask_restx import Namespace, Resource
from app.blueprints.common.pagination import paginate
from app.blueprints.business.v1.dependent.models import Dependent
from app.blueprints.business.v1.dependent.schemas import dependents_schema

api = Namespace('dependents', description='')


@api.route('/')
class DependentList(Resource):
    def get(self):
        departament = Dependent.query.all()
        result = dependents_schema.dump(departament)
        data = paginate(
            query=Dependent.query,
            result=result,
            page=request.args.get('page', 1, type=int),
            per_page=min(request.args.get('per_page', 10, type=int), 100),
            endpoint='bp_v1.dependents_dependent_list'
        )
        return data, 200