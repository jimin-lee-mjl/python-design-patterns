from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import Model, BaseQuery
from pymongo import MongoClient


class MongoAlchemyQuery(BaseQuery, MongoClient):
    def get(self, ident):
        """pk값으로 row 가져오기"""
        return self.find_one({'_id': ident})

    def filter_by(self, **kwargs):
        """kwarg값으로 row 가져오기"""
        return self.find({**kwargs})

    def first(self):
        return self.find()[0]


def main():
    app = Flask(__name__)

    # db client 설정
    client = MongoClient('mongodb://localhost:27017')
    db = client['study']
    col = db.user

    # orm 사용을 위한 sqlalchemy 설정 
    sql = SQLAlchemy(app, query_class=MongoAlchemyQuery)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mongodb://{client.address[0]}:{client.address[1]}/{db.name}'

    class User(Model):
        name = sql.Column(sql.String(15), nullable=False)
        age = sql.Column(sql.Integer, nullable=True)

    users = [
        {'name': 'anne', 'age':16},
        {'name': 'diana', 'age':16},
    ]
    col.insert_many(users)

    anne = User.query.filter_by(name='anne').first()
    print(anne)


main()
