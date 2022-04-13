CREATE TABLE IF NOT EXISTS category(
    id SERIAL PRIMARY KEY,
    name  VARCHAR(250) UNIQUE,
    created_at TIMESTAMP --Add some autoincrement wey to fill values--
);

CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    author INTEGER PRIMARY KEY,
    category INTEGER PRIMARY KEY,
    published_ad DATE

);

CREATE TABLE IF NOT EXISTS authors(
    id SERIAL PRIMARY KEY
    name varchar,
    year_of_birth DATE
)