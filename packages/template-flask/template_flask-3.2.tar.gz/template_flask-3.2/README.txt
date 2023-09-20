# template-flask

pip install template_flask


from the command line navigate to the directory where you would like to keep your project

type "python -m template_flask" and click enter

enter the name of your project

once completed you will have a basic flask directory structure setup and a virtual environment with these packages installed within it...

atomicwrites
attrs
blinker
click
colorama
coverage
Flask
Flask-DebugToolbar
Flask-Login
Flask-Mail
Flask-SQLAlchemy
Flask-WTF
greenlet
gunicorn
iniconfig
itsdangerous
Jinja2
MarkupSafe
packaging
pluggy
py
pyparsing
pytest
pytest-cov
SQLAlchemy
tomli
Werkzeug
WTForms


Directory structure
<your_app>

--> <your_app>_app (main app module)

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


Within the templates and static folders that are created, you will find HTML, CSS, and JS for various Bootstrap 5 example
if you would like to use them in your project.

To preview the live Bootstrap pages, activate your newly created virtual environment and
run the newly created "run.py" file from within your new project directory, open to
the index page and click through the buttons.


