from apmp import app, db
from apmp.models import Client, Admin
from flask import render_template, redirect, url_for, request, flash
from apmp.forms import LoginFormClient, LoginFormAdmin, AddClientForm, MessageForm

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    msgForm = MessageForm()
    return render_template('home.html', msgForm=msgForm)

@app.route('/about', methods=['GET', 'POST'])
def about():
    msgForm = MessageForm()
    return render_template('about.html', msgForm=msgForm)

@app.route('/products', methods=['GET', 'POST'])
def products():
    msgForm = MessageForm()
    return render_template('products.html', msgForm=msgForm)

@app.route('/services', methods=['GET', 'POST'])
def services():
    msgForm = MessageForm()
    return render_template('services.html', msgForm=msgForm)

@app.route('/events', methods=['GET', 'POST'])
def events():
    msgForm = MessageForm()
    return render_template('events.html', msgForm=msgForm)

@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    msgForm = MessageForm()
    return render_template('contact_us.html', msgForm=msgForm)

@app.route('/login_client', methods=['GET', 'POST'])
def login_client():
    loginFormClient = LoginFormClient()
    
    if request.method == 'POST':
        client_id = loginFormClient.client_id.data
        password = loginFormClient.password.data

        attempted_client = Client.query.filter_by(client_id=client_id).first()

        if attempted_client:
            if attempted_client and attempted_client.password_hash == password:
                return redirect(url_for('client', client_id=client_id))
            else:
                flash(f'Incorrect username or password.', category='danger')
        else:
            flash(f'The client ID you entered isn’t connected to an account.', category='warning')

    return render_template('login/client.html', loginFormClient=loginFormClient)

@app.route('/login_admin', methods=['GET', 'POST'])
def login_admin():
    loginFormAdmin = LoginFormAdmin()
    
    if request.method == 'POST':
        username = loginFormAdmin.username.data
        password = loginFormAdmin.password.data

        attempted_admin = Admin.query.filter_by(username=username).first()

        if attempted_admin:
            if attempted_admin and attempted_admin.password == password:
                return redirect(url_for('admin', username=username))
            else:
                flash(f'Incorrect username or password.', category='danger')
        else:
            flash(f'The username you entered isn’t connected to an account.', category='warning')
    return render_template('login/admin.html', loginFormAdmin=loginFormAdmin)

@app.route('/admin<username>')
def admin(username):
    admin = Admin.query.filter_by(username=username).first()

    fname = admin.first_name
    mname = admin.middle_name
    lname = admin.last_name

    admin_name = f'{fname} {mname} {lname}'

    return render_template('admin/admin.html', admin_name=admin_name)

@app.route('/client<client_id>')
def client(client_id):
    client = Client.query.filter_by(client_id=client_id).first()

    fname = client.first_name
    mname = client.middle_name
    lname = client.last_name

    client_name = f'{fname} {mname} {lname}'

    return render_template('client/client.html', client_name=client_name)

@app.route('/admin/add_client', methods=['GET', 'POST'])
def add_client():
    add_client_form = AddClientForm()

    if request.method == 'POST':
        if add_client_form.validate_on_submit():
            client_to_create = Client()
            
            client_to_create.first_name = add_client_form.first_name.data
            client_to_create.middle_name = add_client_form.middle_name.data
            client_to_create.last_name = add_client_form.last_name.data
            client_to_create.email = add_client_form.email.data
            client_to_create.address = add_client_form.address.data
            client_to_create.mobile_number = add_client_form.mobile_number.data
            client_to_create.sex = add_client_form.sex.data
            client_to_create.age = add_client_form.age.data
            client_to_create.birth_date = add_client_form.birth_date.data
            client_to_create.password = add_client_form.password.data

            db.session.add(client_to_create)
            db.session.commit()

            
    return render_template('admin/add_client.html', add_client_form=add_client_form)