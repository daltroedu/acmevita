from flask_migrate import Migrate

migrate = Migrate()

from app.blueprints.business.v1.departament import models
from app.blueprints.business.v1.dependent import models
from app.blueprints.business.v1.employee import models