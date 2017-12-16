from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import markdown
import bleach
from config import Config
from .views.admin import admin_panel
#from .views.api import api

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

app.jinja_env.filters['markdown'] = lambda text: markdown.markdown(bleach.clean(text), extensions=['markdown.extensions.tables'])


from .views.home import app 

app.register_blueprint(admin_panel, url_prefix="/admin")
#app.register_blueprint(api, url_prefix="/api")
