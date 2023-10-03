"""
The flask application package.
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))





app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///kemzapp.db'
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir,'kemzapp.db')
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'kemzapp.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False



db = SQLAlchemy(app)
migrate = Migrate(app, db)

import ecomz.views
import ecomz.models
import ecomz.forms
