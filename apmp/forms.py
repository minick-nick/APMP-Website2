from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TelField, EmailField, TextAreaField, IntegerField, DateField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError


class LoginFormClient(FlaskForm):
    client_id = StringField(label='Client ID', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')

class LoginFormAdmin(FlaskForm):
    username= StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')

class AddClientForm(FlaskForm):
    first_name= StringField(label='First Name', validators=[DataRequired()])
    middle_name= StringField(label='Middle Name', validators=[DataRequired()])
    last_name= StringField(label='Last Name', validators=[DataRequired()])
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    address = StringField(label="Address", validators=[DataRequired()])
    mobile_number = StringField(label="Mobile Number", validators=[DataRequired()])
    sex = StringField(label="Sex", validators=[DataRequired()])
    age = IntegerField(label="Age", validators=[DataRequired()])
    birth_date = DateField(label="Birth Date", validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Register')


class MessageForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    contact_number = TelField(label='Contact number', validators=[DataRequired()])
    message = TextAreaField(label='Message', validators=[DataRequired()])
    submit = SubmitField(label='Send')