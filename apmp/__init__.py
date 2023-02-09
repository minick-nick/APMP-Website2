from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdfsdfsdfsdfsdfsdfsdfsd' # This secre key should be random. Change this later.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///apmp.db'

db = SQLAlchemy(app)

from apmp import routes

