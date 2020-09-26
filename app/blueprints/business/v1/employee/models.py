import uuid
from sqlalchemy.dialects.postgresql import UUID
from app.extensions.database import db
from app.blueprints.business.v1.dependent.models import Dependent


class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())
    full_name = db.Column(db.String(64), nullable=False, index=True)
    departament_id = db.Column(UUID(as_uuid=True), db.ForeignKey('departament.id'), nullable=False)
    have_dependents = db.Column(db.Boolean(), nullable=False)
    dependent = db.relationship(Dependent, backref='employee', lazy='dynamic', cascade='all, delete-orphan')

    def __init__(self, data):
        self.full_name = data['full_name']
        self.departament_id = data['departament_id']
        self.have_dependents = data['have_dependents']

    def __repr__(self):
        return f'<Employee {self.id}>'