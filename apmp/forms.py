from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TelField, EmailField, TextAreaField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError


class LoginForm(FlaskForm):
    emailOrNumber = StringField(label='Email or number', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')

class MessageForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    contact_number = TelField(label='Contact number', validators=[DataRequired()])
    message = TextAreaField(label='Message', validators=[DataRequired()])
    submit = SubmitField(label='Send')