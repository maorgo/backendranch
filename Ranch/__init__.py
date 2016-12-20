from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import settings
import os

conf = settings.Configure()


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = conf.database_connection_string
app.config["SECRET_KEY"] = conf.secret_key
db = SQLAlchemy(app)

import views
