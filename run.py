from flask import Flask
from app import create_app

app = Flask(__name__)

# Run Server
if __name__ == '__main__':
    create_app(app)
    app.run(debug=True)
