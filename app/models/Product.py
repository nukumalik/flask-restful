from ..config import db, ma


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, description, price, qty, user_id):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty
        self.user_id = user_id


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('name', 'description', 'price', 'qty', 'user_id')


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
