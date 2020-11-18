from .controllers.products import ProductsApi, ProductApi


def resources(api):
    api.add_resource(ProductsApi, '/products')
    api.add_resource(ProductApi, '/product/<int:_id>')
