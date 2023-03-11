from datetime import datetime
import pytz
from sqlalchemy import Identity
from apmp import db, bcrypt, login_manager
from sqlalchemy.schema import Sequence
from flask_login import UserMixin

now = datetime.now(pytz.timezone('Asia/Singapore'))


@login_manager.user_loader
def load_user(user_id):    
    login_manager.login_view = 'login'
    
    if str(user_id).isnumeric():
        return Client.query.get(user_id)
    
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
    lot_type = db.Column(db.String)
    status = db.Column(db.String(length=30))
    owner_id = db.Column(db.Integer, db.ForeignKey('client.client_id'))
    purchase_detail = db.relationship('LotPurchaseDetail', backref='lot', uselist=False)

class LotPurchaseDetail(db.Model):
    purchase_detail_id = db.Column(db.Integer, primary_key=True)
    purchase_type = db.Column(db.String, nullable=False) # if monthly amortization or installment
    selected_promo = db.Column(db.Text)
    # lot_purchase_price = db.Column(db.String) 
    lot_id = db.Column(db.Integer, db.ForeignKey('lot.lot_id'), unique=True)
    monthly_amortization = db.relationship('MonthlyAmortization', backref='lot_purchase_detail', uselist=False)

class MonthlyAmortization(db.Model):
    monthly_amortization_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String, nullable=False)
    num_of_mos_to_pay = db.Column(db.Integer, nullable=False)
    total_payment = db.Column(db.Float, nullable=False)
    monthly_payment = db.Column(db.Float, nullable=False)
    balance = db.Column(db.Float, nullable=False)
    schedule_type = db.Column(db.String, nullable=False)
    payment_schedule = db.Column(db.Text, nullable=False)
    lot_purchase_detail_id = db.Column(db.Integer, db.ForeignKey('lot_purchase_detail.purchase_detail_id'), unique=True)
    payment_history = db.relationship('PaymentHistory', backref='monthly_amortization')


class PaymentHistory(db.Model):
    payment_history_id = db.Column(db.Integer, primary_key=True)
    date_paid = db.Column(db.DateTime, default=now)
    payment_method = db.Column(db.String, nullable=False)
    paid_for_month_of = db.Column(db.String, nullable=False)
    amount_paid = db.Column(db.Float, nullable=False)
    change = db.Column(db.Float)
    remaining_amount_to_pay = db.Column(db.Float, nullable=False)
    monthly_amor_id = db.Column(db.Integer, db.ForeignKey('monthly_amortization.monthly_amortization_id'))


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
    is_spot_cash = db.Column(db.Boolean)
    num_of_mos_to_pay = db.Column(db.Integer)
    list_price = db.Column(db.Float)
    disc_per = db.Column(db.Integer)
    disc_value = db.Column(db.Float)
    perp_care_fund_per = db.Column(db.Integer)
    perp_care_value = db.Column(db.Float)
    vat_per = db.Column(db.Integer)
    vat_val = db.Column(db.Float)
    monthly_pay = db.Column(db.Integer)
    total = db.Column(db.Float)

class NewsContent(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    md_code = db.Column(db.Text)

class AvailableAndNotAvailbaleLots(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phase_num = db.Column(db.Integer, nullable=False)
    lawn_num = db.Column(db.Integer, nullable=False)
    num_of_lots = db.Column(db.Integer, nullable=False)
    IDLOTNUM = db.Column(db.Text, nullable=False)
