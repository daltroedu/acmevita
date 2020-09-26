from flask_restx import fields
from .resources import api

employee_post_model = api.model('EmployeePostModel', {
    'full_name': fields.String(description='Employee name', required=True),
    'departament_id': fields.String(description='Departament UUID', required=True),
    'dependents': fields.List(fields.String)
})

employee_put_model = api.model('EmployeePutModel', {
    'full_name': fields.String(description='Employee name', required=True),
    'departament_id': fields.String(description='Departament UUID', required=True),
})

dependent_model = api.model('DependentModel', {
    'full_name': fields.String(description='Dependent name', required=True),
})