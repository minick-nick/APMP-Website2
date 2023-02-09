from apmp import db

class Client(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    f_name = db.Column(db.String(length=30), nullable=False)
    m_name = db.Column(db.String(length=30), nullable=False)
    l_name = db.Column(db.String(length=30), nullable=False)
    email = db.Column(db.String(length=30), unique=True)
    number = db.Column(db.String(length=15), unique=True)
