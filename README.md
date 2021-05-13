### My Practice Flask Template
```
      _____
     `.___,'
      (___)
      <   >
       ) (
      /`-.\
     /     \
    / _    _\
   :,' `-.' `:
   |         |
   :         ;
    \       /
     `.___.' 
     
```




#To build from scratch





##### INSTALL DEPENDENCIES AND SETUP VENV
```
pipenv install Flask python-dotenv SQLAlchemy Flask-SQLAlchemy psycopg2-binary WTForms Flask-WTF Flask-Login [other_dependency] [etc]
```





##### gitignore
```
curl https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore > .gitignore
```





##### flaskenv
```
FLASK_ENV=development
SECRET_KEY=<mySecretKey>
DATABASE_URL=postgresql://dbUser:dbUserPassword@localhost/dbName
```





##### envExample
```
FLASK_APP=myAppName.py
SQLALCHEMY_TRACK_MODIFICATIONS=False
```





##### routes/myMainRouteFileName.py
```
from flask import Blueprint


bp = Blueprint("myMainRouteFileName", __name__, url_prefix="")


@bp.route("/")
def index():
    return "JD's awesome template for an initially confusing (but ultimately maybe preferred over express?) framework"
```





##### config.py
```
import os


class Configuration:
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
  SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
```




##### app/__init__.py
```
from flask import Flask
from .config import Configuration
from .routes import myMainRouteFileName

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(myMainRouteFileName.bp)
```





##### myAppName.py
```
from app import app
```





##### Run the app
```
pipenv run flask run

OR FROM SHELL

pipenv shell
flask run
```





##### Structure when done
```
projectFolder
|____app
|        __init__.py
|
|____routes
|        __init__.py
|        myMainRouteFileName.py
|
|    .env
|    .flaskenv
|    .gitignore
|    config.py
|    myAppName.py
|    Pipfile
|    Pipfile.lock
```





##### Acknowledgments
I don't do ASCII art
**https://asciiart.website/index.php?art=objects/bottles**
