from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_apispec.extension import FlaskApiSpec
from flask_marshmallow import Marshmallow
from . import app
db = SQLAlchemy()
db.init_app(app)
api = Api(app)
docs = FlaskApiSpec(app)
ma = Marshmallow(app)
base_url = "/v1"