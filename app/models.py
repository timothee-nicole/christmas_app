from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from app import db

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
db.create_all()


class Gift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    description = db.Column(db.String(140))
    user_id = db.Column(db.Integer)
    who_offers_it = db.Column(db.Integer)
    username = db.Column(db.String(140), db.ForeignKey("user.username"))

    def __repr__(self):
        return '<Gift {}>'.format(self.name)


@login.user_loader
def load_user(id):
    return Users.query.get(int(id))

db.create_all()
