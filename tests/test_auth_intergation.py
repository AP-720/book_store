from playwright.sync_api import Page, expect

from app import app
from lib.database_connection import DatabaseConnection


def test_auth_integration():
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/books.sql")

    client = app.test_client()

    response = client.post("/sessions", data={"username": "Test", "password": "Test"})

    assert response.status_code == 302

    result = connection.execute("SELECT * FROM users WHERE username = 'Test'")

    assert len(result) == 1
    assert result[0]["username"] == "Test"

    assert response.headers["Location"].endswith("/books")


def test_auth_integration_failure():
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/books.sql")

    client = app.test_client()

    response = client.post("/sessions", data={"username": "Fail", "password": "Test"})

    assert response.headers["Location"].endswith("/sessions/new")


def test_auth_playwright(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/books.sql")

    page.goto("http://127.0.0.1:5001/sessions/new")
    page.get_by_label("username").fill("Test")
    page.get_by_label("password").fill("Test")
    page.get_by_role("button", name="Submit").click()

    assert page.url == "http://127.0.0.1:5001/books"


def test_auth_playwright_failure(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/books.sql")

    page.goto("http://127.0.0.1:5001/sessions/new")
    page.get_by_label("username").fill("Fail")
    page.get_by_label("password").fill("Fail")
    page.get_by_role("button", name="Submit").click()

    expect(page.get_by_role("heading", name="Login Form")).to_be_visible()
    assert page.url == "http://127.0.0.1:5001/sessions/new"


def test_unauthenticated_user_adding_book(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/books.sql")

    page.goto("http://127.0.0.1:5001/books")
    page.get_by_label("title").fill("The Chronicles of Geronimo (the cat)")
    page.get_by_label("author").fill("Geronimo")
    page.get_by_role("button", name="Submit").click()

    assert page.url == "http://127.0.0.1:5001/sessions/new"

