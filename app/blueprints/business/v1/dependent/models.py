import uuid
from sqlalchemy.dialects.postgresql import UUID
from app.extensions.database import db


class Dependent(db.Model):
    __tablename__ = 'dependent'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())
    full_name = db.Column(db.String(64), nullable=False, index=True)
    employee_id = db.Column(UUID(as_uuid=True), db.ForeignKey('employee.id'), nullable=False)

    def __init__(self, data):
        self.full_name = data['full_name']
        self.employee_id = data['employee_id']

    def __repr__(self):
        return f'<Dependent {self.id}>'