from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
    userid = IntegerField('Identificación', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = IntegerField('Teléfono', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    tipo = StringField('Tipo de usuario', validators=[DataRequired(), Length(max=12)])
    submit = SubmitField('Registrar')


class LoginForm(FlaskForm):
    userid = IntegerField('Identificación', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Ingresar')

class BasicHData(FlaskForm):
    name = StringField('Nombre del hospital', validators=[DataRequired(), Length(max=24)])
    addres = StringField('Dirección del hospital', validators=[DataRequired(), Length(max=24)])
    services = StringField('Servicios ofrecidos', validators=[DataRequired(), Length(max=208)])
    submit = SubmitField('Enviar')    

class BasicUData(FlaskForm):
    name = StringField('Nombre del usuario', validators=[DataRequired(), Length(max=24)])
    addres = StringField('Dirección del usuario', validators=[DataRequired(), Length(max=24)])
    services = StringField('fecha de naciomiento', validators=[DataRequired(), Length(max=208)])
    submit = SubmitField('Ingresar')    