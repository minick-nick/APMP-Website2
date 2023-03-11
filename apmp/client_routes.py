import json
from apmp import app
from apmp.models import MonthlyAmortization, login_manager
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required


@app.route('/client/owned_lot')
@login_required
def client():
    return render_template('client/owned_lot.html')

@app.route('/client/monthly_amortization/<m_amor_id>')
@login_required
def m_amor(m_amor_id):
    m_amor = MonthlyAmortization.query.filter_by(monthly_amortization_id=m_amor_id).first()

    payment_sche = m_amor.payment_schedule
    payment_sche = json.loads(payment_sche)
    payment_sche = payment_sche['SCHEDULE']

    payment_his = m_amor.payment_history


    return render_template('client/monthly_amortization.html', m_amor=m_amor, payment_sche=payment_sche, payment_his=payment_his)

@app.route('/client/map')
@login_required
def client_map():
    return render_template('client/map.html')

@app.route('/client/messages')
@login_required
def messages():
    return render_template('client/messages.html')