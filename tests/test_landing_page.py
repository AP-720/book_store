from lib.database_connection import DatabaseConnection
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("http://127.0.0.1:5001")

    h1 = page.locator("h1")

    expect(h1).to_have_text("Welcome to AceReads")


def test_books_title(page: Page):
    page.goto("http://127.0.0.1:5001/books")

    h1 = page.locator("h1")

    expect(h1).to_have_text("Books")


# def test_books_list(page: Page):
#     page.goto("http://127.0.0.1:5001/books")
#     connection = DatabaseConnection()
#     connection.connect()
#     connection.seed("seeds/schema.sql")

#     li = page.get_by_role("listitem")

#     expect(li).to_have_text(
#         [
#             "The Gruffalo by Julia Donaldson",
#             "Ada Twist, Scientist by Andrea Beaty",
#             "The Girl Who Drank the Moon by Kelly Barnhill",
#             "Dragons in a Bag by Zetta Elliott",
#         ]
#     )
