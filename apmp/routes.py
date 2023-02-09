from apmp import app
from flask import render_template, redirect, url_for, request
from apmp.forms import LoginForm, MessageForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    
    if request.method == 'POST':
        username = loginForm.emailOrNumber.data
        password = loginForm.password.data

        if username != '' and password != '':
            return redirect(url_for('admin', cre={"password": password, "username": username}))

    return render_template('login.html', loginForm=loginForm)

@app.route('/admin<cre>')
def admin(cre):
    return render_template('admin/admin.html', cre=cre)