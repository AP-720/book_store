TRUNCATE table books;

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

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(225),
    password VARCHAR(255)
);

