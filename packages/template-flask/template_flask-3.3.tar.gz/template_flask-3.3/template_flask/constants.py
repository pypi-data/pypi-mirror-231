REQUIREMENTS = [
    'flask',
    'flask_sqlalchemy',
    'flask_login',
    'flask_mail',
    'flask_wtf',
    'flask_debugtoolbar',
    'gunicorn',
    'pytest',
    'pytest_cov'
]

INDEX_HTML = [
    ['<!DOCTYPE html>', False],
    ['<html lang="en">', False],
    ['<head>', False],
    ['\t<meta charset="UTF-8">', False],
    ['\t<title>NEW PROJECT: {app}</title>', True],
    ['</head>', False],
    ['<body>', False],
    ['\t<h1>Welcome to your new project: {app}</h1>', True],
    ['''\t<p><button onclick="Fetcher.fetcher('fetcher', {hello: 'world'});">Click here for asynchronous post</button></p>''', False],
    ['\t<p><h3>Check out the Bootstrap Templates below to add to your project</h3></p>', False],
    ['\t<p><label>The HTML, CSS AND JS for these are located in the TEMPLATES AND STATIC folders</label></p> ', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='album') }}"><b>Album</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='blog') }}"><b>Blog</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='carousel') }}"><b>Carousel</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='cheatsheet') }}"><b>Cheatsheet</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='checkout') }}"><b>Checkout</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='cover') }}"><b>Cover</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='dashboard') }}"><b>Dashboard</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='grid') }}"><b>Grid</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='headers') }}"><b>Headers</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='heroes') }}"><b>Heroes</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='jumbotron') }}"><b>Jumbotron</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='masonry') }}"><b>Masonry</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='navbars') }}"><b>Navbars</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='navbar_bottom') }}"><b>Navbar Bottom</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='navbar_top_fixed') }}"><b>Navbar Top Fixed</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='navbar_top_static') }}"><b>Navbar Top Static</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='pricing') }}"><b>Pricing</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='product') }}"><b>Product</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='sidebars') }}"><b>Sidebars</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='sign_in') }}"><b>Sign In</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='starter_template') }}"><b>Starter Template</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='sticky_footer') }}"><b>Sticky Footer</b></a></p>''', False],
    ['''\t<p><a href="{{ url_for('bootstrap', bs_page='sticky_footer_navbar') }}"><b>Sticky Footer Navbar</b></a></p>''', False],
    ['''\t<script src="{{ url_for('static', filename='js/fetcher.js') }}"></script>''', False],
    ['</body>', False],
    ['</html>', False]
]

CONFIG_INIT = [
    ["", False]
]

CONFIG_CONFIG = [
    ['import os', False],
    ['', False],
    ['', False],
    ['class DevlConfig(object):', False],
    ['\t# Base Configurations', False],
    ['\tSECRET_KEY = """{secret_key}"""', True],
    ["\tENV = 'development'", False],
    ["\tDEBUG = True", False],
    ["\tSESSION_COOKIE_SECURE = False", False],
    ["\tTESTING = True", False],
    ['', False],
    ['\t# Database Configurations', False],
    ['\tSQLALCHEMY_TRACK_MODIFICATIONS = False', False],
    ["\tSQLALCHEMY_DATABASE_URI = 'sqlite:///{app}_db.db'", True],
    ["\t# SQLALCHEMY_DATABASE_URI = 'postgresql://<your_username>:<your_password>@<host>:<port>/<database_name>'", False],
    ["\t# SQLALCHEMY_DATABASE_URI = 'mysql://<your_username>:<your_password>@<host>:<port>/<database_name>", False],
    ["\t# SQLALCHEMY_DATABASE_URI = 'oracle://<your_username>:<your_password>@<host>:<port>/<sid_name>", False],
    ['', False],
    ["\t# Flask Mail Config", False],
    ["\t# MAIL_SERVER = ''\t# Your Mail Server (ex. 'smtp.zoho.com')", False],
    ["\t# MAIL_PORT = ''\t# Your Mail Port (ex. 465)", False],
    ["\t# MAIL_USE_SSL = ''\t# Using SSL? (True/False)", False],
    ["\t# MAIL_USE_TLS = ''\t# Using TLS? (True/False)", False],
    ["\t# MAIL_USERNAME = ''\t# Your Mail Email Address (ex. 'admin@yourcompany.com')", False],
    ["\t# MAIL_PASSWORD = ''\t# Your Mail Password", False],
    ["\t# MAIL_DEFAULT_SENDER = ''\t# Your Mail Default Sender (ex. 'admin@yourcompany.com')", False],
    ['', False],
    ['\t# Custom Configurations', False],
    ["\tBASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))", False],
    ["\tSERVER_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))", False],
    ['', False],
    ['', False],
    ['class ProdConfig(DevlConfig):', False],
    ['\t# Base Configurations', False],
    ["\tENV = 'production'", False],
    ["\tDEBUG = False", False],
    ["\t# SESSION_COOKIE_SECURE = True  # Include this when you have an SSL certificate", False],
    ["\tTESTING = False", False],
    ['', False],
    ['\t# Database Configurations', False],
    ["\t# SQLALCHEMY_DATABASE_URI = 'sqlite:///{app}_db.db'", True],
    ["\tSQLALCHEMY_DATABASE_URI = 'postgresql://<your_username>:<your_password>@<host>:<port>/<database_name>'", False],
    ["\t# SQLALCHEMY_DATABASE_URI = 'mysql://<your_username>:<your_password>@<host>:<port>/<database_name>", False],
    ["\t# SQLALCHEMY_DATABASE_URI = 'oracle://<your_username>:<your_password>@<host>:<port>/<sid_name>", False],
    ['', False],
    ['\t# Custom Configurations', False],
    ['', False],
    ['', False]
]

MODEL_INIT_HINT = [
    ['', False]
]

MODEL_INIT = [
    ["# Import all Flask-SQLAlchemy Models to here and then the main __init__.py will import * (all) from here", False],
    ["", False],
    ["", False],
    ["from .db import db", False],
    ["from .user import User", False],
    ["from .other_model import OtherModel", False]
]

MODEL_DB = [
    ["from datetime import datetime", False],
    ["from flask_sqlalchemy import SQLAlchemy", False],
    ["from sqlalchemy.ext.hybrid import hybrid_property", False],
    ["", False],
    ["", False],
    ["# Shared Database (db) for models and tables in seperated .py files.", False],
    ["# models.__init__.py imports db and other Flask-SQLAlchemy Models and", False],
    ["# then the main __init__.py for the app will import * (all) from app.models.", False],
    ["", False],
    ["", False],
    ["db = SQLAlchemy()", False]
]

MODEL_DATATYPES = [
    ["from hashlib import sha256", False],
    ["from sqlalchemy.types import TypeDecorator, String", False],
    ["", False],
    ["", False],
    ["# Here you can create custom Column Datatypes for Flask-SQLAlchemy Models", False],
    ["", False],
    ["", False],
    ["class Name(TypeDecorator):", False],
    ["\timpl = String(128)  # The implied class type from SQLAlchemy", False],
    ["", False],
    ["\tdef process_bind_param(self, value, dialect):", False],
    ["\t\t#This method will process the value upon creation and can transform it before inserting into database", False],
    ["\t\treturn value.lower().capitalize()", False],
    ["", False],
    ["\tdef process_result_value(self, value, dialect):", False],
    ["\t\t#This method will process the value upon loading and can transform it before the Model attribute is set", False],
    ["\t\treturn value", False],
    ["", False],
    ["", False],
    ["class Password(TypeDecorator):", False],
    ["\timpl = String(64)  # The implied class type from SQLAlchemy", False],
    ["", False],
    ["\tdef process_bind_param(self, value, dialect):", False],
    ["\t\t#This method will process the value upon creation and can transform it before inserting into database", False],
    ["\t\treturn sha256(value.encode('utf-8')).hexdigest()", False],
    ["", False],
    ["\tdef process_result_value(self, value, dialect):", False],
    ["\t\t#This method will process the value upon loading and can transform it before the Model attribute is set", False],
    ["\t\treturn value", False]
]

MODEL_USER = [
    ["from .db import db, datetime, hybrid_property", False],
    ["from .datatypes import Name, Password", False],
    ["", False],
    ["", False],
    ["# Example User Model", False],
    ["# When creating more Models in separate python files, go to <app>.models.__init__.py and import the new model to there.", False],
    ["# The main __init__.py for the app will import * (all) from <app>.models.__init__.py ", False],
    ["", False],
    ["", False],
    ["class User(db.Model):", False],
    ["\tid = db.Column(db.Integer, primary_key=True)", False],
    ["\tdate_created = db.Column(db.DateTime, nullable=False, default=datetime.now())", False],
    ["\tfirst_name = db.Column(Name)  # From datatypes.py - Custom datatype which will capitalize the name upon creation", False],
    ["\tlast_name = db.Column(Name)  # From datatypes.py - Custom datatype which will capitalize the name upon creation", False],
    ["\temail = db.Column(db.String(128))", False],
    ["\tusername = db.Column(db.String(64), unique=True)", False],
    ["\tpassword = db.Column(Password)  # From datatypes.py - Custom datatype which will convert password to sha256 hexdigest", False],
    ["", False],
    ["\t@hybrid_property", False],
    ["\tdef full_name(self):", False],
    ["\t\treturn f'{self.first_name} {self.last_name}'", False]
]

MODEL_OTHER_MODEL = [
    ["from datetime import datetime", False],
    ["from .db import db, datetime", False],
    ["", False],
    ["", False],
    ["# Other Example Model", False],
    ["# When creating more Models in separate python files, go to <app>.models.__init__.py and import the new model to there.", False],
    ["# The main __init__.py for the app will import * (all) from <app>.models.__init__.py ", False],
    ["", False],
    ["", False],
    ["class OtherModel(db.Model):", False],
    ["\t__tablename__ = 'other_model'", False],
    ["\tid = db.Column(db.Integer, primary_key=True)", False],
    ["\tdate_created = db.Column(db.DateTime, nullable=False, default=datetime.now())", False]
]


ROUTE_INIT = [
    ["", False]
]

ROUTE_ROUTE = [
    ["from flask import render_template, redirect, url_for, request, session, flash, jsonify, make_response", False],
    ["from {app}_app import app, db, User, OtherModel", True],
    ["", False],
    ["", False],
    ["@app.route('/', methods=['POST', 'GET'])", False],
    ["@app.route('/home', methods=['POST', 'GET'])", False],
    ["def index():", False],
    ["\tif request.method == 'POST':", False],
    ["\t\tprint(request.form)", False],
    ["\t\tprint(request.files)", False],
    ["\treturn render_template('index.html')", False],
    ["", False],
    ["", False],
    ["@app.route('/bootstrap_<bs_page>')", False],
    ["def bootstrap(bs_page):", False],
    ["\treturn render_template(f'bootstrap/{bs_page}.html')", False],
    ["", False],
    ["", False],
    ["# Asynchronous route using the Fetcher Object in static/js/fetcher.js", False],
    ["# Customize this object for use in your application", False],
    ["@app.route('/fetcher', methods=['POST'])", False],
    ["def fetcher():", False],
    ["\tpost = request.get_json()", False],
    ["\tprint('fetcher post = ', post)", False],
    ["\tresponse = make_response(jsonify({'message': 'good response', 'data': {'hello': True, 'world': [1, 2, 3]}}), 200)", False],
    ["\treturn response", False]
]


RUN = [
    ["from {app}_app import app", True],
    ["", False],
    ["app = app  # For gunicorn", False],
    ["", False],
    ["if __name__ == '__main__':", False],
    ["\tif app.debug:", False],
    ["\t\tHOST = None  # Flask will use defaults", False],
    ["\t\tPORT = None", False],
    ["\telse:", False],
    ["\t\tHOST = 'local_host'", False],
    ["\t\tPORT = 5001", False],
    ["", False],
    ["\tapp.run(host=HOST, port=PORT)", False],
]

INIT = [
    ["from flask import Flask", False],
    ["# from flask_login import ()", False],
    ["# from flask_mail import ()", False],
    ["# from flask_wft import ()", False],
    ["# from flask_debugtoolbar import ()", False],
    ["from datetime import timedelta", False],
    ["", False],
    ["from .config.config import *", False],
    ["from .models import *", False],
    ["", False],
    ["", False],
    ["app = Flask(__name__)", False],
    ["app.permanent_session_lifetime = timedelta(seconds=600)  # Timeout for session objects", False],
    ["", False],
    ["", False],
    ["ENV = 'devl'  # OR 'prod'", False],
    ["", False],
    ["if ENV == 'prod':", False],
    ["\tapp.config.from_object(ProdConfig)  # From .config.config", False],
    ["else:", False],
    ["\tapp.config.from_object(DevlConfig)", False],
    ["", False],
    ["", False],
    ["with app.app_context():", False],
    ["\tdb.init_app(app)", False],
    ["\t# db.create_all()", False],
    ["", False],
    ["", False],
    ["from .routes import routes", False]
]

JS_FETCHER = [
    ["// Global Instance of Fetcher", False],
    ["// This object can send asynchronous requests to your Flask routes", False],
    ["// Main use - Fetcher.fetcher(route_url_endpoint, data to be posted, method (default is POST))", False],
    ["", False],
    ["(function (global) {", False],
    ['\t"use strict";', False],
    ["\tlet lastFetch = {};", False],
    ["\tlet lastFetchEndpoint = null;", False],
    ["\tlet lastFetchUrl = null;", False],
    ["\tlet lastFetchBody = null;", False],
    ["\tlet lastFetchMethod = null;", False],
    ["", False],
    ["\tlet fetcher = function(url_endpoint, body, method='POST'){", False],
    ["\t\t// Update last fetch properties", False],
    ["\t\tlastFetchEndpoint = url_endpoint;", False],
    ["\t\tlastFetchUrl = `${window.origin}/${url_endpoint}`;", False],
    ["\t\tlastFetchBody = body;", False],
    ["\t\tlastFetchMethod = method;", False],
    ["\t\tlastFetch = {", False],
    ["\t\t\torigin: window.origin,", False],
    ["\t\t\tendpoint: lastFetchEndpoint,", False],
    ["\t\t\turl: lastFetchUrl,", False],
    ["\t\t\tbody: lastFetchBody,", False],
    ["\t\t\tmethod: lastFetchMethod", False],
    ["\t\t};", False],
    ["", False],
    ["\t\t// Start fetching process to Flask route", False],
    ["\t\tfetch(lastFetchUrl, {", False],
    ["\t\t\tmethod: lastFetchMethod,", False],
    ["\t\t\tcredentials: 'include',", False],
    ["\t\t\tbody: JSON.stringify(lastFetchBody),", False],
    ["\t\t\tcache: 'no-cache',", False],
    ["\t\t\theaders: new Headers({", False],
    ["\t\t\t\t'content-type': 'application/json'", False],
    ["\t\t\t})", False],
    ["\t\t})", False],
    ["\t\t.then(function(response) {", False],
    ["\t\t\t// You can customize .then function as needed", False],
    ["\t\t\tif (response.status !== 200) {", False],
    ["\t\t\t\talert(`Response was not 200: ${response.status} - at ${lastFetchUrl}`);", False],
    ["\t\t\t} else {", False],
    ["\t\t\t\tresponse.json().then(function(data){", False],
    ["\t\t\t\t\t// data from flask.make_response", False],
    ["\t\t\t\t\tlet alert_text = `A javascript object called Fetcher (located at static/js/fetcher.js) can be called to make asynchronous posts to your Flask app you can edit this object to suit the needs of your app\\n\\ndata sent: ${JSON.stringify(lastFetch)}\\n\\ndata received: ${JSON.stringify(data)}`;", False],
    ["\t\t\t\t\talert(alert_text);", False],
    ["\t\t\t\t\tconsole.log('data sent: ', lastFetch);", False],
    ["\t\t\t\t\tconsole.log('data received: ', data);", False],
    ["\t\t\t\t\treturn;", False],
    ["\t\t\t\t})", False],
    ["\t\t\t}", False],
    ["\t\t})", False],
    ["\t};", False],
    ["", False],
    ["", False],
    ["\tlet Fetcher = function(){};", False],
    ["\tObject.assign(Fetcher.prototype, {", False],
    ["\t\tlastFetch: lastFetch,", False],
    ["\t\tlastFetchEndpoint: lastFetchEndpoint,", False],
    ["\t\tlastFetchUrl: lastFetchUrl,", False],
    ["\t\tlastFetchBody: lastFetchBody,", False],
    ["\t\tlastFetchMethod: lastFetchMethod,", False],
    ["", False],
    ["\t\tfetcher: function(url_endpoint, body, method='POST'){", False],
    ["\t\t\tfetcher(url_endpoint, body, method);", False],
    ["\t\t}", False],
    ["\t});", False],
    ["", False],
    ["\tglobal.Fetcher = new Fetcher;", False],
    ["", False],
    ["})(this);", False],
    ["", False]
]

DOCKERFILE = [
    ['FROM python:{py_version}', True],
    ["", False],
    ['RUN apt-get update && apt-get upgrade', False],
    ["", False],
    ['WORKDIR /{app}', True],
    ["", False],
    ['COPY requirements.txt requirements.txt', False],
    ["", False],
    ['RUN pip3 install -r requirements.txt', False],
    ["", False],
    ['COPY . .', False],
    ["", False],
    ['EXPOSE 5001', False],
    ["", False],
    ['CMD gunicorn -w 4 --bind 0.0.0.0:5001 wsgi:app', False]
]

DOCKERIGNORE = [
    ['/__pycache__', False],
    ['/instance', False],
    ['/venv', False],
    ['/.idea', False]
]

DIRECTORY_STRUCTURE = """
Directory structure

{app}

--> {app}_app (main app module)

    --> __init__.py (flask app configuration and imports)
    
    --> config
        --> __init__.py
        --> config.py
        
    --> models
        --> __init__.py
        --> datatypes.py
        --> db.py
        --> other_model.py
        --> user.py
        
    --> routes
        --> __init__.py
        --> routes.py
        
    --> static
        --> css
            --> bootstrap
                --> * all bootstrap example css
        --> img
        --> js
            --> bootstrap
                --> * all bootstrap example js
            fetcher.js
            
    --> templates
        --> bootstrap
            --> * all bootstrap example html
        --> index.html
        
--> venv
--> requirements.txt
--> wsgi.py (main flask app entry point)
--> Dockerfile
--> .dockerignore

"""
