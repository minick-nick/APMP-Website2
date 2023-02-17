from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdfsdfsdfsdfsdfsdfsdfsd' # This secret key should be random. Change this later.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/apmp_db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

#from apmp import db_c
#db_c('c')

def db_c(flag):
    app.app_context().push()
    
    if flag == 'c':
        db.create_all()
        from apmp.models import Admin
        from apmp.models import LotPromo
        from apmp import LOT

        a = Admin()
        a.username = "dom"
        a.name = "dom"
        a.password = "password"

        db.session.add(a)
        db.session.commit()

        for promo in LOT.PROMOS:
            p = LotPromo()

            p.type = promo['TYPE']
            p.label = promo['LABEL']
            p.is_spot_cash = promo['IS_SPOT_CASH']
            p.num_of_mos_to_pay = promo['NUM_OF_MOS_TO_PAY']
            p.list_price = promo['LIST_PRICE']
            p.disc_per = promo['DISC_PER']
            p.disc_value = promo['DISC_VALUE']
            p.perp_care_fund_per = promo['PERP_CARE_FUND_PER']
            p.perp_care_value = promo['PERP_CARE_VALUE']
            p.vat_per = promo['VAT_PER']
            p.vat_val = promo['VAT_VAL']
            p.monthly_pay = promo['MONTHLY_PAY']
            p.total = promo['TOTAL']
            
            db.session.add(p)
            db.session.commit()

        print('db created')

    elif flag == 'd':
        db.drop_all()
        print('db droped')

CLIENT_ID_START = 10000000

from apmp import general_routes
from apmp import admin_routes
from apmp import client_routes

