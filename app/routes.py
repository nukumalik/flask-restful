from .controllers.products import ProductsApi, ProductApi
from .controllers.users import LoginApi, RegisterApi, UserApi


def resources(api):
    api.add_resource(ProductsApi, '/products')
    api.add_resource(ProductApi, '/product/<int:_id>')
    api.add_resource(LoginApi, '/login')
    api.add_resource(RegisterApi, '/register')
    api.add_resource(UserApi, '/user/<int:_id>')
