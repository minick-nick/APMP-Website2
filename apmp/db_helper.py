from apmp import db, app
from apmp.models import VisitorMessage, LotPromo
from flask import flash
import sqlalchemy as sa
from apmp import connection_uri

def push_visitor_message(msg_form):
    v_msg = VisitorMessage()

    v_msg.name = msg_form.name.data
    v_msg.email = msg_form.email.data
    v_msg.mobile_number = msg_form.contact_number.data
    v_msg.message = msg_form.message.data

    try:
        db.session.add(v_msg)
        db.session.commit()
        flash(f'Message sent', category='success')
    except:
        flash(f'Message is not sent. Please try again later.')

def get_downpayment_promos(is_spot_cash):
    
    selected_promo_list = list()

    with app.app_context():
        if table_exists(LotPromo.__tablename__):
            with app.app_context():
                promo_list = LotPromo.query.filter_by(is_spot_cash=is_spot_cash)

                for x in promo_list:
                    id = x.lot_promo_id
                    type = x.type
                    label = x.label
                    selected_promo_list.append((id, f'{type} - {label}'))
                return selected_promo_list
    return [None, None]


def table_exists(name):
    engine = sa.create_engine(connection_uri)
    insp = sa.inspect(engine)
    return insp.has_table(name)