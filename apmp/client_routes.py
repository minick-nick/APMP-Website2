from apmp import app, db
from apmp import CLIENT_ID_START
from apmp.models import Client, Admin, Lot, VisitorMessage, login_manager
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from apmp.forms import LoginFormClient, LoginFormAdmin, AddClientForm, MessageForm
from apmp.db_helper import push_visitor_message



@app.route('/login_client', methods=['GET', 'POST'])
def login_client():
    loginFormClient = LoginFormClient()
    
    if request.method == 'POST':
        if loginFormClient.validate_on_submit():
            client_id = loginFormClient.client_id.data
            password = loginFormClient.password.data

            attempted_client = Client.query.filter_by(client_id=client_id).first()

            if attempted_client:
                if attempted_client and attempted_client.check_password_correction(password):
                    login_user(attempted_client)
                    return redirect(url_for('client'))
                else:
                    flash(f'Incorrect username or password.', category='danger')
            else:
                flash(f'The client ID you entered isn’t connected to an account.', category='warning')

    return render_template('login/client.html', loginFormClient=loginFormClient)



# routes related to client
@app.route('/client/owned_lot')
@login_required
def client():
    return render_template('client/owned_lot.html')

@app.route('/client/monthly_amortization')
@login_required
def monthly_amortization():
    return render_template('client/monthly_amortization.html')

@app.route('/client/map')
@login_required
def client_map():
    return render_template('client/map.html')

@app.route('/client/messages')
@login_required
def messages():
    return render_template('client/messages.html')