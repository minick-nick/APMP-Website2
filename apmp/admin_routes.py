from apmp import app, db
from apmp import CLIENT_ID_START
from apmp.models import Client, Admin, Lot, VisitorMessage, LotPromo, NewsContent, login_manager
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from apmp.forms import LoginFormClient, LoginFormAdmin, AddClientForm, MessageForm, LotPromoForm, LotPromoForm, NewsContentForm
from apmp.db_helper import push_visitor_message
from markdown import markdown
from apmp.util import modify_html_code


@app.route('/login_admin', methods=['GET', 'POST'])
def login_admin():
    loginFormAdmin = LoginFormAdmin()
    
    if request.method == 'POST':
        if loginFormAdmin.validate_on_submit:
            username = loginFormAdmin.username.data
            password = loginFormAdmin.password.data

            attempted_admin = Admin.query.filter_by(username=username).first()

            if attempted_admin:
                if attempted_admin and attempted_admin.check_password_correction(password):
                    login_user(attempted_admin)
                    return redirect(url_for('admin'))
                else:
                    flash(f'Incorrect username or password.', category='danger')
            else:
                flash(f'The username you entered isn’t connected to an account.', category='warning')
    return render_template('login/admin.html', loginFormAdmin=loginFormAdmin)

@app.route('/admin/dashboard')
@login_required
def admin():
    return render_template('admin/dashboard.html')

@app.route('/admin/clients')
@login_required
def clients():
    clients = Client.query.all()
    return render_template('admin/clients.html', clients=clients)

@app.route('/admin/queries/visitors')
@login_required
def visitors_queries():
    visitors_msgs = VisitorMessage.query.all()

    for visitor_msg in visitors_msgs:
        visitor_msg.date_received = str(visitor_msg.date_received).split()[0]

    return render_template('admin/queries/visitors.html', visitors_msgs=visitors_msgs)

@app.route('/admin/lot_image_request')
@login_required
def lot_image_request():
    return render_template('admin/lot_image_request.html')

@app.route('/admin/map')
@login_required
def map():
    return render_template('admin/map.html')

@app.route('/admin/add_client', methods=['GET', 'POST'])
@login_required
def add_client():
    add_client_form = AddClientForm()

    if request.method == 'POST':
        if add_client_form.validate_on_submit():
            client = Client()
            client_lot = Lot()
            
            client.first_name = add_client_form.first_name.data
            client.middle_name = add_client_form.middle_name.data
            client.last_name = add_client_form.last_name.data
            client.email = add_client_form.email.data
            client.mobile_number = add_client_form.mobile_number.data
            client.address = add_client_form.address.data
            client.birth_date = add_client_form.birth_date.data
            client.name_of_spouse = add_client_form.name_of_spouse.data
            client.password = add_client_form.password.data
            
            # if the client table is empty 
            if Client.query.filter_by(client_id=CLIENT_ID_START).first() == None:
                client.client_id = CLIENT_ID_START

            client_lot.phase_number = add_client_form.phase_number.data
            client_lot.lawn_number = add_client_form.lawn_number.data
            client_lot.lot_number = add_client_form.lot_number.data
            client_lot.status = add_client_form.lot_status.data
            client_lot.client = client

            
            db.session.add(client, client_lot)
            db.session.commit()

            flash(f'{client.first_name} {client.last_name} is successfully registered.', category='success')
            
            return redirect(url_for('clients'))

    if add_client_form.errors != {}:
        for err_msg in add_client_form.errors.values():

            flash(f'{err_msg}', category='warning')

    return render_template('admin/forms/add_client_form.html', add_client_form=add_client_form)

@app.route('/admin/edit_website_content/interest_promo', methods=['POST', 'GET'])
@login_required
def edit_interest_promo():
    PROMOS = LotPromo.query.order_by(LotPromo.lot_promo_id)
    lot_promo_form = LotPromoForm()

    if request.method == 'POST':
        if lot_promo_form.validate_on_submit:

            edit_promo = request.form.get('edit_promo')
            promo = LotPromo.query.filter_by(lot_promo_id=edit_promo).first()

            if promo:
                promo.label = lot_promo_form.label.data
                promo.num_of_mos_to_pay = lot_promo_form.num_of_mos_to_pay.data
                promo.list_price = lot_promo_form.list_price.data
                promo.disc_price = lot_promo_form.disc_per.data
                promo.disc_value = lot_promo_form.disc_value.data
                promo.perp_care_fund_per = lot_promo_form.perp_care_fund_per.data
                promo.perp_care_value = lot_promo_form.perp_care_value.data
                promo.vat_per = lot_promo_form.vat_per.data
                promo.vat_val = lot_promo_form.vat_val.data
                promo.total = lot_promo_form.total.data
                promo.monthly_pay = lot_promo_form.monthly_pay.data
                
                db.session.commit()

                return redirect(url_for('edit_interest_promo'))

    return render_template('admin/website_content/edit_interest_promo.html', PROMOS=PROMOS, 
    lot_promo_form=lot_promo_form)


@app.route('/admin/edit_website_content/edit_news', methods=['POST', 'GET'])
@login_required
def edit_news():
    current_md_code =  NewsContent.query.filter_by(id=1).first()
    news_content_form = NewsContentForm()


    if request.method == 'POST':
        if news_content_form.validate_on_submit:
            current_md_code.md_code = news_content_form.md_code.data
            db.session.commit()
            return redirect('edit_news')
    
    news_content_form.md_code.data = current_md_code.md_code
    html_code = markdown(current_md_code.md_code)
    news = modify_html_code(html_code)

    return render_template('admin/website_content/edit_news.html', news=news, news_content_form=news_content_form)
    