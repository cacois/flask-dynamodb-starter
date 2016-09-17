import datetime
from app.server import app, db, bcrypt
from flywheel import Model, Field
from datetime import datetime

class User(Model):

    __tablename__ = "users"

    email = Field(type=str, hash_key=True, nullable=False)
    password = Field(type=str, nullable=False)
    registered_on = Field(type=datetime, nullable=False)
    admin = Field(type=bool, nullable=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        )
        self.registered_on = datetime.now()
        self.admin = admin

    def is_authenticated(self):
        # TODO implement me
        return True

    def is_active(self):
        # TODO implement me
        return True

    def is_anonymous(self):
        # TODO implement me
        return False

    def get_id(self):
        return self.email

    def __repr__(self):
        return '<User {0}>'.format(self.email)
