# Flask example

Using Flask to build a Restful API Server with Swagger document.

Integration with Flask-Cors, Flask-Testing and Flask-SQLalchemy

### Extension:
- SQL ORM: [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.1/)

- Testing: [Flask-Testing](http://flask.pocoo.org/docs/0.12/testing/)

## Installation

Install with pip:

```
$ pip install -r requirements.txt
```

## Flask Configuration

#### Example

```
app = Flask(__name__)
app.config['DEBUG'] = True
```
 
## Run Flask
### Run flask for develop
```
$ python application.py
```
In flask, Default port is `5000`


## Run Testing
```
$ python -m pytest
```