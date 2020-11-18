from ..config import db, ma
from flask_jwt import JWT
from werkzeug.security import check_password_hash
from flask import Flask

app = Flask(__name__)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password


class UserSchema(ma.Schema):
    class Meta:
        fields = ('email', 'password')


def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return user


def identity(payload):
    _id = payload['identity']
    return User.query.get(_id)


jwt = JWT(app, authenticate, identity)


user_schema = UserSchema()
users_schema = UserSchema(many=True)
