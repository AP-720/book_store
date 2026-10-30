from flask import Flask, redirect, render_template, request
from lib.book import Book
from lib.book_repository import BookRepository
from lib.database_connection import DatabaseConnection
from lib.film import Film
from lib.film_repository import FilmRepository
from lib.user import User
from lib.user_repository import UserRepository

# instantiate a Flask app object
app = Flask(__name__)


# Declares a route that listens for a GET request to the path /hello
# and a method to execute when that request comes in
# @app.route("/hello", methods=["GET"])
# def hello():
#     return "Hello to you too"


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# Books


@app.route("/books", methods=["GET"])
def get_all_books():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    books = book_repository.all()
    return render_template("books.html", books=books)


@app.route("/books", methods=["POST"])
def post_book():
    book_details = request.form
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    book = Book(title=book_details["title"], author=book_details["author"])
    book_repository.create(book)
    return redirect("/books")


# Films


@app.route("/films", methods=["GET"])
def get_films():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    films = film_repository.all()
    return render_template("films.html", films=films)

@app.route("/films/new", methods=["POST"])
def add_new_film():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)

    film_details = request.form
    film = Film(title=film_details["title"], genre=film_details["genre"])
    film_repository.save(film)

    return redirect("/films")



# Sign up


@app.route("/users", methods=["GET"])
def get_sign_up():
    return render_template("signup_form.html")


@app.route("/users/new", methods=["POST"])
def create_user():
    user_details = request.form
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    user = User(username=user_details["username"], password=user_details["password"])
    user_repository.create(user)
    return redirect("/")


# Authors


@app.route("/authors", methods=["GET"])
def authors():
    return [
        {"name": "Julia Donaldson", "dob": "1948-09-16"},
        {"name": "Andrea Beaty", "dob": "1961-10-08"},
        {"name": "Kelly Barnhill", "dob": "1973-01-01"},
        {"name": "Zetta Elliott", "dob": "1979-11-11"},
    ]


@app.route("/team", methods=["GET"])
def get_team():
    team = ["Dorothy", "Rose", "Blanche", "Sophia"]
    return render_template("team.html", team=team)


# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
