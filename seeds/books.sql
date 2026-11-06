-- Books
DROP TABLE IF EXISTS books;

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL
);

INSERT INTO
    books (title, author)
VALUES
    ('The Gruffalo', 'Julia Donaldson');

INSERT INTO
    books (title, author)
VALUES
    ('Ada Twist, Scientist', 'Andrea Beaty');

INSERT INTO
    books (title, author)
VALUES
    ('The Girl Who Drank the Moon', 'Kelly Barnhill');

INSERT INTO
    books (title, author)
VALUES
    ('Dragons in a Bag', 'Zetta Elliott');

-- Films
DROP TABLE IF EXISTS films;

CREATE TABLE IF NOT EXISTS films (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255)
);

TRUNCATE TABLE films;

INSERT INTO
    films (title, genre)
VALUES
    ('The Grand Budapest Hotel', 'Comedy');

INSERT INTO
    films (title, genre)
VALUES
    ('Interstellar', 'Sci-Fi');

INSERT INTO
    films (title, genre)
VALUES
    ('Get Out', 'Horror');

-- Users
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(225),
    password VARCHAR(255)
);

INSERT INTO
    users (username, password)
VALUES
    ('Test', 'Test');
