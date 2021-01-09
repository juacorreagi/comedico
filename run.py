from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from forms import SignupForm, LoginForm, BasicHData, BasicUData
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://julio:prog@localhost:5432/comedico'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager(app) #Objeto de la clase LoginManager
login_manager.login_view = "login" #Redirigir el usuario
db = SQLAlchemy(app)

from models import User

bootstrap = Bootstrap(app) #Inicializar Bootstrap

@app.route('/')
@login_required
def index():    
    return render_template('index.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_userid(form.userid.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template('login.html', form=form)

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('index'))        
    form = SignupForm()
    error = None
    if form.validate_on_submit():
        userid = form.userid.data
        email = form.email.data
        phone = form.phone.data
        password = form.password.data
        tipo = form.tipo.data
      
        user = User.get_by_email(email)
        if user is not None: # Comprobamos que no hay un usuario con ese email
            error = f'El email {email} ya está siendo utilizado por otro usuario'
        else:            
            user = User(userid=userid, phone=phone, email=email, tipo=tipo) # Creamos el usuario y lo guardamos
            user.set_password(password)
            user.save()
            
            login_user(user, remember=True) # Dejamos al usuario logueado
            next_page = request.args.get('next', None)
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template("signup_form.html", form=form, error=error)

 
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))  