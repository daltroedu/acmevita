import uuid
from sqlalchemy.dialects.postgresql import UUID
from app.extensions.database import db
from app.blueprints.business.v1.employee.models import Employee


class Departament(db.Model):
    __tablename__ = 'departament'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())
    name = db.Column(db.String(64), nullable=False, unique=True, index=True)
    employee = db.relationship(Employee, backref='departament', lazy='dynamic')

    def __init__(self, data):
        self.name = data['name']

    def __repr__(self):
        return f'<Departament {self.id}>'