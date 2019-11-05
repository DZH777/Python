import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    books = db.relationship("Book", backref="author", lazy=True)
    
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=True)
    id_author = db.Column(db.Integer, db.ForeignKey("authors.id"), nullable=True)
