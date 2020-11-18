from ..models.User import user_schema, User
from ..config import db
from flask_restful import Resource
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash


# Login
class LoginApi(Resource):
    def post(self):
        email = request.json['email']
        password = request.json['password']
        if email is None:
            return {'message': 'Email must be filled'}
        if password is None:
            return {'message': 'Password must be filled'}

        user = User.query.get(email)
        if user is None:
            return {'message': 'Email not registered yet'}

        isMatch = check_password_hash(user['password'], password)
        if isMatch is False:
            return {'message': 'Password is invalid'}

        return {'message': 'Success login to account', 'data': user}


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
        return {'message': 'Success register new account', 'data': new_user}


class UserApi(Resource):
    def put(self, _id):
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

    def delete(self, _id):
        user = User.query.get(_id)
        if user is None:
            return {'message': 'User is not found'}

        db.session.delete(user)
        db.session.commit()
        return {'message': 'Success delete an user', 'data': user}
