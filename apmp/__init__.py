from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdfsdfsdfsdfsdfsdfsdfsd' # This secre key should be random. Change this later.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///apmp.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from apmp import routes

