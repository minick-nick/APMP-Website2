from apmp import app, db
from apmp.models import LotPromo, NewsContent, Admin, Client, login_manager
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user
from apmp.forms import LoginForm, MessageForm
from apmp.db_helper import push_visitor_message
from markdown import markdown
from apmp.util import modify_html_code, is_client_number

@app.route('/',  methods=['GET', 'POST'])
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



@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    
    if request.method == 'POST':
        if loginForm.validate_on_submit:
            key = loginForm.username_or_client_id.data
            password = loginForm.password.data

            key = key.replace('-', '')
            
            if is_client_number(key):
                
                attempted_client = Client.query.filter_by(client_id=key).first()

                if attempted_client:
                    if attempted_client and attempted_client.check_password_correction(password):
                        login_user(attempted_client)
                        return redirect(url_for('client'))
                    else:
                        flash(f'Incorrect client ID or password.', category='danger')
                else:
                    flash(f'The client ID you entered isn’t connected to an account.', category='warning')


            else:      
                attempted_admin = Admin.query.filter_by(username=key).first()

                if attempted_admin:
                    if attempted_admin and attempted_admin.check_password_correction(password):
                        login_user(attempted_admin)
                        return redirect(url_for('admin'))
                    else:
                        flash(f'Incorrect username or password.', category='danger')
                else:
                    flash(f'The username you entered isn’t connected to an account.', category='warning')

    return render_template('sign_in.html', loginForm=loginForm)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
