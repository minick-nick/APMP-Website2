from apmp import db
from apmp.models import VisitorMessage
from flask import flash

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

