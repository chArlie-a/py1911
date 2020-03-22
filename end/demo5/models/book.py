# Charlie
# date:2020/3/16 17:48
# file_name:book
from .utils import db
from sqlalchemy import column, ForeignKey
from sqlalchemy.orm import relationship, backref


class Category(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return self.name


class Book(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(50), nullable=False, unique=True)
    # 定义外键
    cid = db.Column('cid', db.ForeignKey('category.id', ondelete='CASCADE'), nullable=False)
    category = db.relationship('Category', backref='books')

    def __repr__(self):
        return self.name
