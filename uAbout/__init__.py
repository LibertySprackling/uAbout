import bcrypt
from dotenv import load_dotenv
from os import environ
from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt

from .database.db import db
from .routes.main import main_routes
from .routes.auth import auth_routes

load_dotenv()

database_uri=environ.get('DATABASE_URL')
if 'postgres' in database_uri:
    database_uri=database_uri.replace('postgres:', 'postgresql:')

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_NOTIFICATIONS=environ.get('SQL_ALCEHMY_TRACK_MODIFICATIONS'),
    SQLALCHEMY_ECHO=True
)

bcrypt = Bcrypt(app)
CORS(app)
db.app=app
db.init_app(app)



app.register_blueprint(main_routes)
app.register_blueprint(auth_routes)

if __name__ == "__main__":
    app.run(debug=True)