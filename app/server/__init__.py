# app/server/__init__.py
import os

from flask import Flask, render_template
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flywheel import Engine

################
#### config ####
################

app = Flask(
    __name__,
    template_folder='../client/templates',
    static_folder='../client/static'
)

app_settings = os.getenv('APP_SETTINGS', 'app.server.config.DevelopmentConfig')
app.config.from_object(app_settings)

####################
#### extensions ####
####################

login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)
toolbar = DebugToolbarExtension(app)
bootstrap = Bootstrap(app)
db = Engine()

###################
### setup db ####
###################
from app.server.models import User

print("Connecting to DynamoDB instance: {}".format(app.config.get('DYNAMODB_HOST')))
db.connect_to_host(host=app.config.get('DYNAMODB_HOST'),port=8000)
print("Registering models...")
db.register(User)

###################
### blueprints ####
###################

from app.server.views.user import user_blueprint
from app.server.views.main import main_blueprint
app.register_blueprint(user_blueprint)
app.register_blueprint(main_blueprint)

###################
### flask-login ####
###################

login_manager.login_view = "user.login"
login_manager.login_message_category = 'danger'

@login_manager.user_loader
def load_user(email):
    # TODO fix me
    return db.query(User).filter(User.email == email).first()

########################
#### error handlers ####
########################

@app.errorhandler(401)
def forbidden_page(error):
    return render_template("errors/401.html"), 401

@app.errorhandler(403)
def forbidden_page(error):
    return render_template("errors/403.html"), 403

@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404

@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500
