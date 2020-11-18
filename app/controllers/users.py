from ..models.User import user_schema, User
from ..config import db
from flask_restful import Resource
from flask import request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta


# Login
class LoginApi(Resource):
    def post(self):
        email = request.json['email']
        password = request.json['password']
        if email is None:
            return {'message': 'Email must be filled'}
        if password is None:
            return {'message': 'Password must be filled'}

        user = User.query.filter_by(email=email).first()
        if user is None:
            return {'message': 'Email not registered yet'}
        isMatch = check_password_hash(user.password, password)
        if isMatch is False:
            return {'message': 'Password is invalid'}
        expires_delta = timedelta(days=1)
        access_token = create_access_token(
            identity=user.id, fresh=True, expires_delta=expires_delta)
        return {'message': 'Success login to account', 'access_token': access_token}


class RegisterApi(Resource):
    def post(self):
        email = request.json['email']
        password = request.json['password']
        if email is None:
            return {'message': 'Email must be filled'}
        if password is None:
            return {'message': 'Password must be filled'}

        hash_password = generate_password_hash(password)
        new_user = User(email, hash_password)
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'Success register new account'}


class UserApi(Resource):
    @jwt_required
    def put(self):
        _id = get_jwt_identity()
        user = User.query.get(_id)
        if user is None:
            return {'message': 'User is not found'}

        email = request.json['email']
        password = request.json['password']

        if email is None:
            return {'message': 'Email must be filled'}
        if password is None:
            return {'message': 'Password must be filled'}

        hash_password = generate_password_hash(password)

        user.email = email
        user.password = hash_password
        db.session.commit()
        return user_schema.jsonify(user)

    @jwt_required
    def delete(self):
        _id = get_jwt_identity()
        user = User.query.get(_id)
        if user is None:
            return {'message': 'User is not found'}

        db.session.delete(user)
        db.session.commit()
        return {'message': 'Success delete an user', 'data': user}
