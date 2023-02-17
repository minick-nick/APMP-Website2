from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TelField, EmailField, TextAreaField, IntegerField, DateField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from apmp.models import Client, Lot

from apmp import LOT

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
    mobile_number = StringField(label="Mobile Number", validators=[DataRequired()])
    address = StringField(label="Address", validators=[DataRequired()])
    birth_date = DateField(label="Birth Date", validators=[DataRequired()])
    name_of_spouse = StringField(label="Name of spouse", validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    lot_status = SelectField(label='Status', choices=LOT.LOT_STATUS)
    phase_number = IntegerField(label='Phase number', validators=[DataRequired()])
    lawn_number = IntegerField(label='Lawn number', validators=[DataRequired()])
    lot_number = IntegerField(label='Lot number', validators=[DataRequired()])

    submit = SubmitField(label='Save')

    def validate_phase_number(self, phase_number):
        if int(phase_number.data) < 1 or int(phase_number.data) > 2:
            raise ValidationError("Invalid phase number. Pleaese select phase number between 1 and 2 only.")

    # to-do: make validation for lawn number and lot number

    def validate_email(self, email):
        email_found = Client.query.filter_by(email=email.data).first()

        if email_found:
            raise ValidationError('Email already exists! Please try a different email.')

    def validate_mobile_number(self, mobile_number):
        mobile_number_found = Client.query.filter_by(mobile_number=mobile_number.data).first()

        if mobile_number_found:
            raise ValidationError('Mobile number already exists! Please try a different mobile number.')
            
class MessageForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    contact_number = TelField(label='Contact number', validators=[DataRequired()])
    message = TextAreaField(label='Message', validators=[DataRequired()])
    submit = SubmitField(label='Send')