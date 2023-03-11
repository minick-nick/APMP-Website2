import json
from apmp import db, app
from apmp.models import AvailableAndNotAvailbaleLots, VisitorMessage, LotPromo
from flask import flash
import sqlalchemy as sa
from apmp import connection_uri

def push_visitor_message(msg_form):
    v_msg = VisitorMessage()

    v_msg.name = msg_form.name.data
    v_msg.email = msg_form.email.data
    v_msg.mobile_number = msg_form.contact_number.data
    v_msg.message = msg_form.message.data
    v_msg.replied = False

    try:
        db.session.add(v_msg)
        db.session.commit()
        flash(f'Message sent', category='success')
    except:
        flash(f'Message is not sent. Please try again later.')

def get_downpayment_promos(is_spot_cash):
    
    selected_promo_list = list()

    if table_exists(LotPromo.__tablename__):
        with app.app_context():       
            promo_list = LotPromo.query.filter_by(is_spot_cash=is_spot_cash)

            for x in promo_list:
                id = x.lot_promo_id
                type = x.type
                label = x.label
                selected_promo_list.append((id, f'{type} - {label}'))
    
        return selected_promo_list
            

def table_exists(name):
    engine = sa.create_engine(connection_uri)
    insp = sa.inspect(engine)
    return insp.has_table(name)


def get_lots(phase_num, lawn_num, available):
    x = AvailableAndNotAvailbaleLots.query.filter_by(phase_num=phase_num, lawn_num=lawn_num).first()
    id_lot_num = json.loads(x.IDLOTNUM)
    id_lot_num = id_lot_num['IDLOTNUM']

    if id_lot_num:
        if available:
            return [[id, lot_num, status] for id, lot_num, status in id_lot_num if id == None]
        else:
            return [[id, lot_num, status] for id, lot_num, status in id_lot_num if id != None]


def get_all_lots(phase_num, lawn_num):
    x = AvailableAndNotAvailbaleLots.query.filter_by(phase_num=phase_num, lawn_num=lawn_num).first()
    id_lot_num = json.loads(x.IDLOTNUM)
    
    return id_lot_num['IDLOTNUM']



def make_lot_unavail(phase_num, lawn_num, lot_num, lot_id, lot_status):
    x = AvailableAndNotAvailbaleLots.query.filter_by(phase_num=phase_num, lawn_num=lawn_num).first()
    id_lot_num = json.loads(x.IDLOTNUM)
    id_lot_num = id_lot_num['IDLOTNUM']
       
    for y in id_lot_num:
        if y[1] == lot_num:
            y[0] = lot_id
            y[2] = lot_status 

            x.IDLOTNUM = json.dumps({'IDLOTNUM' : id_lot_num})
            print(x.IDLOTNUM)
            db.session.commit()