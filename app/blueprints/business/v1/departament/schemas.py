from app.extensions.schema import ma
from .models import Departament


class DepartamentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Departament
        include_relationships = True
        load_instance = True

    id = ma.auto_field()
    name = ma.auto_field()


departament_schema = DepartamentSchema()
departaments_schema = DepartamentSchema(many=True)