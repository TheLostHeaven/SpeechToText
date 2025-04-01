from flask import Flask, jsonify
from src.routers.voice import voice
from config import Config, DATABASE_CONNECTION_URI, DATABASE_CONNECTION_URI_TEST
from src.utils.db import db
from flask_sqlalchemy import SQLAlchemy



def app_create(testing=False):
    app = Flask(__name__)

    if testing:
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI_TEST
        app.config['TESTING'] = True


    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI

    app.config.from_object(Config)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    app.register_blueprint(voice)


    return app