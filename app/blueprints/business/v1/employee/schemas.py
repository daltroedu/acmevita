from app.extensions.schema import ma
from .models import Employee


class EmployeeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Employee
        include_relationships = True
        load_instance = True

    id = ma.auto_field()
    full_name = ma.auto_field()
    departament_id = ma.auto_field()
    have_dependents = ma.auto_field()


employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)