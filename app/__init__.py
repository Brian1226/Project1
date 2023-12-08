import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail

path = os.path.abspath(os.getcwd()+"/app/database/database.db")
app = Flask(__name__)

app.config["SECRET_KEY"] = "12cf392707648385ca40917f"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'testuseremail2024@gmail.com'
app.config['MAIL_PASSWORD'] = 'ovvp rmhh svay nvkw'
mail = Mail(app)

login_manager  = LoginManager(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

@app.before_first_request
def create_tables(): 
    db.create_all()

from app import routes, models, forms