from flask import Blueprint
from flask_restx import Api

bp = Blueprint('bp_v1', __name__, url_prefix='/v1')
api = Api(bp, title='ACMEVita API', version='1.0', description='')

from .departament.resources import api as departament
from .dependent.resources import api as dependent
from .employee.resources import api as employee

api.add_namespace(departament)
api.add_namespace(dependent)
api.add_namespace(employee)