from apmp import db, bcrypt
from sqlalchemy.schema import Sequence

class Admin(db.Model):
    username = db.Column(db.String(length=20), primary_key=True)
    first_name = db.Column(db.String(length=30), nullable=False)
    middle_name = db.Column(db.String(length=30), nullable=False)
    last_name = db.Column(db.String(length=30), nullable=False)
    email = db.Column(db.String(length=30), unique=True, nullable=False)
    address = db.Column(db.String(length=50), nullable=False)
    mobile_number = db.Column(db.String(length=15), unique=True, nullable=False)
    sex = db.Column(db.String(length=10), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    birth_date = db.Column(db.String(length=20), nullable=False)
    password = db.Column(db.String(), nullable=False)


class Client(db.Model):
    client_id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(length=30), nullable=False)
    middle_name = db.Column(db.String(length=30), nullable=False)
    last_name = db.Column(db.String(length=30), nullable=False)
    email = db.Column(db.String(length=30), unique=True, nullable=False)
    address = db.Column(db.String(length=50), nullable=False)
    mobile_number = db.Column(db.String(length=15), unique=True, nullable=False)
    sex = db.Column(db.String(length=10), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    birth_date = db.Column(db.String(length=20), nullable=False)
    password_hash = db.Column(db.String(), nullable=False)

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
