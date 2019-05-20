from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
import os
from flask_htpasswd import HtPasswdAuth

app = Flask(__name__)
app.config.from_object(Config)


app.config['FLASK_HTPASSWD_PATH'] = '.htpasswd'
app.config['FLASK_SECRET'] = 'Hey Hey Kids, secure me!'

htpasswd = HtPasswdAuth(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
basedir = os.path.abspath(os.path.dirname(__file__))
bootstrap = Bootstrap(app)


from app import routes, models
