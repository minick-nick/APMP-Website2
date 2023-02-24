from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import sqlalchemy as sa

app = Flask(__name__)
app.app_context().push()

connection_uri = 'postgresql://postgres:password@localhost/apmp_db'
app.config['SECRET_KEY'] = 'sdfsdfsdfsdfsdfsdfsdfsd' # This secret key should be random. Change this later.
app.config['SQLALCHEMY_DATABASE_URI'] = connection_uri

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

engine = sa.create_engine(connection_uri)
insp = sa.inspect(engine)


def db_c(flag):

    with app.app_context():
        if flag == 'c':
            db.create_all()
            from apmp.models import Admin, LotPromo, NewsContent
            from apmp import CONSTANTS

            a = Admin()
            a.username = "dom"
            a.name = "dom"
            a.password = "password"

            db.session.add(a)
            db.session.commit()

            for promo in CONSTANTS.LOT.PROMOS:
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

            news_content = NewsContent()
            news_content.md_code = CONSTANTS.NEWS
            
            db.session.add(news_content)
            db.session.commit()

            print('db created and initialized')

        elif flag == 'd':
            db.drop_all()
            print('db droped')

from apmp import general_routes
from apmp import admin_routes
from apmp import client_routes

