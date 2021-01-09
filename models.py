from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from run import db

class User(db.Model, UserMixin):
    __tablename__ = 'usu_comedic'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, unique=True, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    tipo = db.Column(db.String(128),  nullable=False)
    
    def __repr__(self):
        return f'<User {self.email}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_by_id(id):
        return User.query.get(id)
    
    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

        
    @staticmethod
    def get_by_userid(userid):
        return User.query.filter_by(userid=userid).first()

    @staticmethod
    def get_by_tipo(tipo):
        return User.query.filter_by(tipo=tipo).first()