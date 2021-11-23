from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine

app = Flask(__name__)
db = MongoEngine(app)
sql_db = SQLAlchemy()

app.config['MONGODB_SETTINGS'] = {
    'db': 'study',
    'host': '127.0.0.1',
    'port': 27017,
}


class User(sql_db.Model):
    name = sql_db.Column(sql_db.String(15), nullable=False)
    age = sql_db.Column(sql_db.Integer, nullable=True)


class User(db.Document):
    name = db.StringField(max_length=15, required=True)
    age = db.IntegerField()


class MongoAlchemy(sql_db):
    def __init__(self, model_class=A
    
    
    , **kwargs) -> None:
        super().__init__(**kwargs)
