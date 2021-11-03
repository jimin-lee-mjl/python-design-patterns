from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import Model
from pymongo import MongoClient

app = Flask(__name__)

sql = SQLAlchemy()
client = MongoClient('mongodb://localhost:27017')
db = client['study']


class User(sql.Model):
    name = sql.Column(sql.String(15), nullable=False)
    age = sql.Column(sql.Integer, nullable=True)



class MongoAlchemy(Model):
    pass
