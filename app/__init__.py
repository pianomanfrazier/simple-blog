from flask import Flask
import markdown
import bleach
from .views.admin import admin_panel
#from .views.api import api

app = Flask(__name__)

app.jinja_env.filters['markdown'] = lambda text: markdown.markdown(bleach.clean(text), extensions=['markdown.extensions.tables'])

from .views.home import app 

app.register_blueprint(admin_panel, url_prefix="/admin")
#app.register_blueprint(api, url_prefix="/api")
