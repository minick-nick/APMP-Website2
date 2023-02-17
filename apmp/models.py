from datetime import datetime
import pytz
from apmp import db, bcrypt, login_manager
from sqlalchemy.schema import Sequence
from flask_login import UserMixin

now = datetime.now(pytz.timezone('Asia/Singapore'))


@login_manager.user_loader
def load_user(user_id):
    if isinstance(user_id, int):
        login_manager.login_view = 'login_client'
        return Client.query.get(user_id)
    
    login_manager.login_view = 'login_admin'
    return Admin.query.get(user_id)

class Admin(db.Model, UserMixin):
    username = db.Column(db.String(length=20), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    """
    middle_name = db.Column(db.String(length=30), nullable=False)
    last_name = db.Column(db.String(length=30), nullable=False)
    email = db.Column(db.String(length=30), unique=True, nullable=False)
    address = db.Column(db.String(length=50), nullable=False)
    mobile_number = db.Column(db.String(length=15), unique=True, nullable=False)
    sex = db.Column(db.String(length=10), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    birth_date = db.Column(db.String(length=20), nullable=False)
    """
    password_hash = db.Column(db.String(), nullable=False)

    def get_id(self):
        return self.username

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
    

class Client(db.Model, UserMixin):
    client_id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(length=30), nullable=False)
    middle_name = db.Column(db.String(length=30), nullable=False)
    last_name = db.Column(db.String(length=30), nullable=False)
    email = db.Column(db.String(length=30), unique=True, nullable=False)
    mobile_number = db.Column(db.String(length=15), unique=True, nullable=False)
    address = db.Column(db.String(length=50), nullable=False)
    birth_date = db.Column(db.String(length=20), nullable=False)
    name_of_spouse = db.Column(db.String(length=20))
    password_hash = db.Column(db.String(), nullable=False)
    owned_lots = db.relationship('Lot', backref='client')

    def get_id(self):
        return self.client_id

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Lot(db.Model):
    lot_id = db.Column(db.Integer, primary_key=True)
    lot_number = db.Column(db.Integer, nullable=False)
    lawn_number = db.Column(db.Integer, nullable=False)
    phase_number = db.Column(db.Integer)
    status = db.Column(db.String(length=30))
    lot_type = db.Column(db.String(length=30))
    lot_price = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('client.client_id'))

class VisitorMessage(db.Model):
    message_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    email = db.Column(db.String(length=30), nullable=False)
    mobile_number = db.Column(db.String(length=15), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_received = db.Column(db.DateTime,default=now)
    replied = db.Column(db.Boolean)
    date_replied = db.Column(db.DateTime)

class LotPromo(db.Model):
    lot_promo_id =  db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    label = db.Column(db.String)
    is_spot_cash = db.Column(db.String)
    num_of_mos_to_pay = db.Column(db.String)
    list_price = db.Column(db.String)
    disc_per = db.Column(db.String)
    disc_value = db.Column(db.String)
    perp_care_fund_per = db.Column(db.String)
    perp_care_value = db.Column(db.String)
    vat_per = db.Column(db.String)
    vat_val = db.Column(db.String)
    monthly_pay = db.Column(db.String)
    total = db.Column(db.String)
    