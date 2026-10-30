from lib.database_connection import DatabaseConnection
from playwright.sync_api import Page, expect


def test_films_has_heading(page: Page):
    page.goto("http://127.0.0.1:5001/films")
    h1 = page.locator("h1")
    expect(h1).to_have_text("Films List")


def test_list_of_films_has_all_films(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/books.sql")
    page.goto("http://127.0.0.1:5001/films")
    li = page.get_by_role("listitem")
    expect(li).to_have_text(
        ["The Grand Budapest Hotel, Comedy", "Interstellar, Sci-Fi", "Get Out, Horror"]
    )


def test_add_new_film(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/books.sql")

    page.goto("http://127.0.0.1:5001/films")
    page.get_by_label("title").fill("Top Gun")
    page.get_by_label("genre").fill("Action")
    page.get_by_role("button", name="Submit").click()

    films = page.locator("li")
    new_film = films.all_inner_texts()[-1]
    assert new_film == "Top Gun, Action"
