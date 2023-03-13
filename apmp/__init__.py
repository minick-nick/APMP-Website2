import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import sqlalchemy as sa
from apmp.CONSTANTS import LOT
from flask_mail import Mail

app = Flask(__name__)

#connection_uri = 'postgresql://postgres:password@localhost/apmp_db'
#for external connection
#connection_uri = 'postgresql://apmp_db_test_user:A2KtDznZHpGFHiu57JmIH8O5SLPSkDpg@dpg-cftma4h4reb6ks0r32ng-a.singapore-postgres.render.com/apmp_db_test'

# For internal connection in render.com
connection_uri = 'postgresql://apmp_db_test_user:A2KtDznZHpGFHiu57JmIH8O5SLPSkDpg@dpg-cftma4h4reb6ks0r32ng-a/apmp_db_test'
app.config['SECRET_KEY'] = 'sdfsdfsdfsdfsdfsdfsdfsd' # This secret key should be random. Change this later.
app.config['SQLALCHEMY_DATABASE_URI'] = connection_uri

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'dominicdofredo16@gmail.com'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

engine = sa.create_engine(connection_uri)
insp = sa.inspect(engine)


app.app_context().push()


def db_c(flag):

    with app.app_context():
        if flag == 'c':
            db.create_all()
            from apmp.models import Admin, LotPromo, NewsContent, AvailableAndNotAvailbaleLots
            from apmp import CONSTANTS

            a = Admin()
            a.username = "dom"
            a.name = "Dominic Dofredo"
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


            res = list()

            p1lawn1 = AvailableAndNotAvailbaleLots()
            max = LOT.PHASE_1.LAWN_1_NUM_OF_LOTS
            x = [[None, lot_num, ''] for lot_num in range(1, max + 1)]
            p1lawn1.phase_num = 1
            p1lawn1.lawn_num = 1
            p1lawn1.num_of_lots = max
            p1lawn1.IDLOTNUM = json.dumps({"IDLOTNUM": x})
            res.append(p1lawn1)

        
            p1lawn2 = AvailableAndNotAvailbaleLots()
            max = LOT.PHASE_1.LAWN_2_NUM_OF_LOTS
            x = [[None, lot_num, ''] for lot_num in range(1, max + 1)]
            p1lawn2.phase_num = 1
            p1lawn2.lawn_num = 2
            p1lawn2.num_of_lots = max
            p1lawn2.IDLOTNUM = json.dumps({"IDLOTNUM": x})
            res.append(p1lawn2)

            
            p1lawn3 = AvailableAndNotAvailbaleLots()
            max = LOT.PHASE_1.LAWN_3_NUM_OF_LOTS
            x = [[None, lot_num, ''] for lot_num in range(1, max + 1)]
            p1lawn3.phase_num = 1
            p1lawn3.lawn_num = 3
            p1lawn3.num_of_lots = max
            p1lawn3.IDLOTNUM = json.dumps({"IDLOTNUM": x})
            res.append(p1lawn3)

            
            p1lawn4 = AvailableAndNotAvailbaleLots()
            max = LOT.PHASE_1.LAWN_4_NUM_OF_LOTS
            x = [[None, lot_num, ''] for lot_num in range(1, max + 1)]
            p1lawn4.phase_num = 1
            p1lawn4.lawn_num = 4
            p1lawn4.num_of_lots = max
            p1lawn4.IDLOTNUM = json.dumps({"IDLOTNUM": x})
            res.append(p1lawn4)

            p1lawn5 = AvailableAndNotAvailbaleLots()
            max = LOT.PHASE_1.LAWN_5_NUM_OF_LOTS
            x = [[None, lot_num, ''] for lot_num in range(1, max + 1)]
            p1lawn5.phase_num = 1
            p1lawn5.lawn_num = 5
            p1lawn5.num_of_lots = max
            p1lawn5.IDLOTNUM = json.dumps({"IDLOTNUM": x})
            res.append(p1lawn5)

            
            p2lawn1 = AvailableAndNotAvailbaleLots()
            max = LOT.PHASE_2.LAWN_1_NUM_OF_LOTS
            x = [[None, lot_num, ''] for lot_num in range(1, max + 1)]
            p2lawn1.phase_num = 2
            p2lawn1.lawn_num = 1
            p2lawn1.num_of_lots = max
            p2lawn1.IDLOTNUM = json.dumps({"IDLOTNUM": x})
            res.append(p2lawn1)


            p2lawn2 = AvailableAndNotAvailbaleLots()
            max = LOT.PHASE_2.LAWN_2_NUM_OF_LOTS
            x = [[None, lot_num, ''] for lot_num in range(1, max + 1)]
            p2lawn2.phase_num = 2
            p2lawn2.lawn_num = 2
            p2lawn2.num_of_lots = max
            p2lawn2.IDLOTNUM = json.dumps({"IDLOTNUM": x})
            res.append(p2lawn2)

            p2lawn3 = AvailableAndNotAvailbaleLots()
            max = LOT.PHASE_2.LAWN_3_NUM_OF_LOTS
            x = [[None, lot_num, ''] for lot_num in range(1, max + 1)]
            p2lawn3.phase_num = 2
            p2lawn3.lawn_num = 3
            p2lawn3.num_of_lots = max
            p2lawn3.IDLOTNUM = json.dumps({"IDLOTNUM": x})
            res.append(p2lawn3)

            db.session.add_all(res)
            db.session.commit()

            print('db created and initialized')

        elif flag == 'd':
            db.drop_all()
            print('db droped')

from apmp import general_routes
from apmp import admin_routes
from apmp import client_routes

