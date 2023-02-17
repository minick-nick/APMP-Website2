from apmp import app, db
from apmp import CLIENT_ID_START
from apmp.models import Client, Admin, Lot, VisitorMessage, login_manager
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from apmp.forms import LoginFormClient, LoginFormAdmin, AddClientForm, MessageForm
from apmp.db_helper import push_visitor_message



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

@app.route('/admin/edit_website_content/interest_promo')
@login_required
def interest_promo():
    return render_template('admin/website_content/interest_promo.html')


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

@app.route('/admin/edit_website_content')
@login_required
def edit_wesite_content():
    pass