from app import app
from lib.database_connection import DatabaseConnection


def test_create_user_is_saved_to_database():
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/books.sql")
    # create the test client to send requests without using Playwright and a browser
    client = app.test_client()

    # set up a DB connection
    connection = DatabaseConnection()
    connection.connect()

    # send the request
    response = client.post(
        "/users/new", data={"username": "testuser", "password": "password123"}
    )

    # assert that the redirect happened
    assert response.status_code == 302

    # read from the DB
    result = connection.execute("SELECT * FROM users WHERE username = 'testuser'")

    # assert that the user was created
    assert len(result) == 1
    assert result[0]["username"] == "testuser"
