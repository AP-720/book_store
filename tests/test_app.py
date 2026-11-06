import os
import sys

# this line is a bit of a hack which allows us to import app without changing anything else
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from playwright.sync_api import Page, expect

from app import app
from lib.database_connection import DatabaseConnection


# GET /books
def test_get_books_returns_a_200():
    # here's where we make the test client
    client = app.test_client()
    # here's where we make the request
    response = client.get("/books")
    # here's where we assert that the response's status code is 200
    assert response.status_code == 200


def test_get_books_returns_all_the_books(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/books.sql")

    page.goto("http://127.0.0.1:5001/books")
    li = page.get_by_role("listitem")
    expect(li).to_have_text(
        [
            "The Gruffalo by Julia Donaldson",
            "Ada Twist, Scientist by Andrea Beaty",
            "The Girl Who Drank the Moon by Kelly Barnhill",
            "Dragons in a Bag by Zetta Elliott",
        ]
    )


# Authors
def test_get_authors_returns_a_200():
    client = app.test_client()
    response = client.get("/authors")
    assert response.status_code == 200


def test_get_authors_returns_all_the_authors():
    client = app.test_client()
    response = client.get("/authors")

    assert response.json == [
        {"name": "Julia Donaldson", "dob": "1948-09-16"},
        {"name": "Andrea Beaty", "dob": "1961-10-08"},
        {"name": "Kelly Barnhill", "dob": "1973-01-01"},
        {"name": "Zetta Elliott", "dob": "1979-11-11"},
    ]


# Form
def test_form_submits(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/books.sql")

    page.goto("http://127.0.0.1:5001/sessions/new")
    page.get_by_label("username").fill("Test")
    page.get_by_label("password").fill("Test")
    page.get_by_role("button", name="Submit").click()

    page.get_by_label("title").fill("The Chronicles of Geronimo (the cat)")
    page.get_by_label("author").fill("Geronimo")
    page.get_by_role("button", name="Submit").click()
    books = page.get_by_role("listitem")
    new_book = books.all_inner_texts()[-1]
    assert new_book == "The Chronicles of Geronimo (the cat) by Geronimo"
