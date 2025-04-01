from flask import Blueprint 

voice = Blueprint('voice', __name__)

@voice.route('/')
def index():
    return '<h1>Hola Mundo</h1>'