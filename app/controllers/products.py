from ..models.Product import product_schema, products_schema, Product
from ..config import db
from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required


class ProductsApi(Resource):
    def get(self):
        all_product = Product.query.all()
        result = []
        for item in products_schema.dump(all_product):
            item.pop('user_id', None)
            result.append(item)
        return {'data': result}

    @jwt_required
    def post(self):
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']
        qty = request.json['qty']
        user_id = get_jwt_identity()
        new_product = Product(name, description, price, qty, user_id)
        db.session.add(new_product)
        db.session.commit()
        return product_schema.jsonify(new_product)


class ProductApi(Resource):
    def get(self, _id):
        product = Product.query.get(_id)
        result = {
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'qty': product.qty,
        }
        return result

    @jwt_required
    def put(self, _id):
        product = Product.query.get(_id)
        if product is None:
            return {'message': 'Product is not found'}

        user_id = get_jwt_identity()
        if product.user_id != user_id:
            return {'message': 'Unauthorized'}

        name = request.json['name']
        description = request.json['description']
        price = request.json['price']
        qty = request.json['qty']

        product.name = name
        product.description = description
        product.price = price
        product.qty = qty
        db.session.commit()
        return product_schema.jsonify(product)

    @jwt_required
    def delete(self, _id):
        product = Product.query.get(_id)
        if product is None:
            return {'message': 'Product is not found'}

        user_id = get_jwt_identity()
        if product.user_id != user_id:
            return {'message': 'Unauthorized'}

        db.session.delete(product)
        db.session.commit()
        return {'message': 'Success remove product'}
