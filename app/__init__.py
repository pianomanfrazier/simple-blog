from flask import Flask
from .views.admin import admin_panel
#from .views.api import api

app = Flask(__name__)

from .views.home import app 

app.register_blueprint(admin_panel, url_prefix="/admin")
#app.register_blueprint(api, url_prefix="/api")
