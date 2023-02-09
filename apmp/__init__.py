from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdfsdfsdfsdfsdfsdfsdfsd' # This secre key should be random. Change this later.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///apmp.db'

db = SQLAlchemy(app)

from apmp import routes

from apmp.models import Client


c = Client()

c.f_name = 'sdfsdf'
c.m_name = 'sdfsdf'
c.l_name = 'sfsdfsfsdf'
c.number = '101204'
c.email = 'ssdfsdfsdfs'


app.app_context().push()

db.create_all()

db.session.add(c)
db.session.commit()


