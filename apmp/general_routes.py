from apmp import app, db
from apmp import CLIENT_ID_START
from apmp.models import Client, Admin, Lot, VisitorMessage, LotPromo, NewsContent, login_manager
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from apmp.forms import LoginFormClient, LoginFormAdmin, AddClientForm, MessageForm
from apmp.db_helper import push_visitor_message
from apmp import LOT
from markdown import markdown
from apmp.util import modify_html_code

@app.route('/',  methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    msgForm = MessageForm()

    if request.method == 'POST':
        if msgForm.validate_on_submit():
            push_visitor_message(msgForm)

            return redirect(url_for('home'))

    return render_template('home.html', msgForm=msgForm)

@app.route('/about', methods=['GET', 'POST'])
def about():
    msgForm = MessageForm()

    if request.method == 'POST':
        if msgForm.validate_on_submit():
            push_visitor_message(msgForm)

            return redirect(url_for('home'))

    return render_template('about.html', msgForm=msgForm)

@app.route('/products', methods=['GET', 'POST'])
def products():
    msgForm = MessageForm()

    if request.method == 'POST':
        if msgForm.validate_on_submit():
            push_visitor_message(msgForm)

            return redirect(url_for('home'))

    return render_template('products.html', msgForm=msgForm)

@app.route('/services', methods=['GET', 'POST'])
def services():
    msgForm = MessageForm()

    if request.method == 'POST':
        if msgForm.validate_on_submit():
            push_visitor_message(msgForm)

            return redirect(url_for('home'))

    return render_template('services.html', msgForm=msgForm)

@app.route('/events', methods=['GET', 'POST'])
def events():
    msgForm = MessageForm()
    current_md_code =  NewsContent.query.filter_by(id=1).first()
    html_code = markdown(current_md_code.md_code)
    news = modify_html_code(html_code)

    if request.method == 'POST':
        if msgForm.validate_on_submit():
            push_visitor_message(msgForm)

            return redirect(url_for('home'))

    return render_template('events.html', news=news, msgForm=msgForm)

@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    msgForm = MessageForm()

    if request.method == 'POST':
        if msgForm.validate_on_submit():
            push_visitor_message(msgForm)

            return redirect(url_for('home'))

    return render_template('contact_us.html', msgForm=msgForm)

@app.route('/interest_promo', methods=['GET', 'POST'])
def interest_pro():
    msgForm = MessageForm()
    PROMOS = LotPromo.query.order_by(LotPromo.lot_promo_id)

    if request.method == 'POST':
        if msgForm.validate_on_submit():
            push_visitor_message(msgForm)

            return redirect(url_for('home'))

    return render_template('interest_promo.html', msgForm=msgForm, PROMOS = PROMOS)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
