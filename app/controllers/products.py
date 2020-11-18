from ..models.Product import product_schema, products_schema, Product
from ..config import db
from flask import jsonify, request
from flask_restful import Resource


class ProductsApi(Resource):
    def get(self):
        all_product = Product.query.all()
        result = products_schema.dump(all_product)
        return jsonify(result)

    def post(self):
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']
        qty = request.json['qty']
        new_product = Product(name, description, price, qty)
        db.session.add(new_product)
        db.session.commit()
        return product_schema.jsonify(new_product)


class ProductApi(Resource):
    def get(self, _id):
        product = Product.query.get(_id)
        return product_schema.jsonify(product)

    def put(self, _id):
        product = Product.query.get(_id)
        if product is None:
            return {'message': 'Product is not found'}
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

    def delete(self, _id):
        product = Product.query.get(_id)
        if product is None:
            return {'message': 'Product is not found'}
        db.session.delete(product)
        db.session.commit()
        return {'message': 'Success remove product'}
