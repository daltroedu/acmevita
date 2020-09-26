from app.extensions.schema import ma
from .models import Dependent


class DependentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Dependent
        include_relationships = True
        load_instance = True

    id = ma.auto_field()
    full_name = ma.auto_field()
    employee_id = ma.auto_field()


dependent_schema = DependentSchema()
dependents_schema = DependentSchema(many=True)