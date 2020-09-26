from flask_restx import fields
from .resources import api

departament_model = api.model('DepartamentModel', {
    'name': fields.String(description='Departament name', required=True),
})