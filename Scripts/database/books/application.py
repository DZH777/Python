import os
import csv

from flask import Flask, render_template, session, redirect, url_for, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
 
app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/import_data")
def import_data():
    f = open("books_short.csv")
    reader = csv.reader(f)
    books = []
    books.append(next(reader, None))
    ##headers = next(reader, None)
    del1 = db.execute("DELETE FROM authors")
    del2 = db.execute("DELETE FROM books")    
    for row in reader:
        ins1 = db.execute("INSERT INTO authors (name) VALUES (:name) ON CONFLICT (name) DO UPDATE SET name=EXCLUDED.name RETURNING id", {"name": row[2]})
        ins2 = db.execute("INSERT INTO books (isbn, title, year, id_author) VALUES (:isbn, :title, :year, :id_author)",
            {"isbn": row[0], "title": row[1], "year": row[3], "id_author": ins1.fetchone()[0]})
        books.append(row)
    db.commit()
    return render_template("import_data.html", books=books)

@app.route("/clear_data")
def clear_data():
    try:
        del1 = db.execute("DELETE FROM authors")
        del2 = db.execute("DELETE FROM books")    
        db.commit()
        message = "Удаление завершено успешно"
    except:
        db.rollback()    
        message = "Удаление завершено не успешно"
    return render_template("clear_data.html", message = message)

@app.route("/search_data", methods=["GET", "POST"])
def search_data():
    books = []
    if request.method == "POST":
        name = request.form.get("name")
        books = db.execute("select b.isbn, b.title, b.year, s.name from books b, authors s where b.id_author = s.id and (lower(b.title) like :name or lower(s.name) like :name)", {"name": '%'+name.lower()+'%'}).fetchall()
        if len(books) > 0:
            title = ["isbn", "title", "year", "name"]
            books.insert(0, title)
        return render_template("search_data.html", books=books)
    else:    
        return render_template("search_data.html")

