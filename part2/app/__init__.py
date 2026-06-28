from flask import Flask
from flask_restx import Api

def create_app():
    app = Flask(__name__)
    api = Api(app, version="1.0", title="NightHunter API",
              description="A dungeon crawler game API")

    # Register namespaces here as you build them
    return app