from flask import Flask, render_template, jsonify, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    tag = request.form.get("str")
    if not tag:
        return render_template("index.html")
    books = Book.query.filter(Book.title.ilike(f'%{tag}%')).all()
    authors = Author.query.filter(Author.name.ilike(f'%{tag}%')).all()
    return render_template("results.html", tag=tag, books=books, authors=authors)
    
@app.route("/book/<int:bid>")
def books(bid):
    book = Book.query.get(bid)
    author = Author.query.filter_by(id=book.id_author).first()
    return render_template("books.html", book=book, author=author)

@app.route("/author/<int:aid>")
def authors(aid):

    author = Author.query.get(aid)
    books = author.books
    return render_template("authors.html", author=author, books=books)


