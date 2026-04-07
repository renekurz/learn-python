from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

class Base(DeclarativeBase):
    pass

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)

# all_books = []

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    books_db = db.session.execute(db.select(Book).order_by(Book.id)).scalars().all()
    return render_template("index.html", books=books_db)


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/submit", methods=["POST"])
def add_book():
    try:
        name = request.form["book_name"]
        author = request.form["book_author"]
        rating = int(request.form["book_rating"])
    except ValueError:
        return render_template("add.html", error="Rating must be a number!")
    else:
        if rating > 10:
            return render_template("add.html", error="Rating must be between 0 and 10!")
        
        new_book = Book(
            title=name,
            author=author,
            rating=rating
        )

        db.session.add(new_book)
        db.session.commit()

        # new_book = {
        #     "title": name,
        #     "author": author,
        #     "rating": rating
        # }

        # all_books.append(new_book)

        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

