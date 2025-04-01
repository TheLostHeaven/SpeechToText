from decouple import config
from dotenv import load_dotenv
# import os 

load_dotenv()

class Config():
    SECRET_KEY = config('SECRET_KEY')


DATABASE_CONNECTION_URI = "sqlite:///transcriptions.db"

DATABASE_CONNECTION_URI_TEST = "sqlite:///transcriptions.db"