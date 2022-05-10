--Countries--
CREATE TABLE IF NOT EXISTS countries(
    id SERIAL,
    name VARCHAR(255) UNIQUE,
    shortcut VARCHAR(2) UNIQUE,
    PRIMARY KEY (id)
);
--Categories--
CREATE TABLE IF NOT EXISTS categories(
    id SERIAL,
    name VARCHAR UNIQUE ,
    PRIMARY KEY (id)
);
--Status--
CREATE TABLE IF NOT EXISTS status(
    id SERIAL,
    name VARCHAR UNIQUE ,
    PRIMARY KEY (id)
);
--Authors--
CREATE TABLE IF NOT EXISTS authors(
    id SERIAL,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    nationality VARCHAR,
    date_of_birt DATE NOT NULL,
    date_of_die DATE,
    PRIMARY KEY (id),
    FOREIGN KEY (nationality)
        REFERENCES countries(shortcut)
);

--Books--
CREATE TABLE IF NOT EXISTS books(
    id SERIAL,
    title VARCHAR,
    author_id INT NOT NULL,
    status_id INTEGER NOT NULL,
    published_at DATE,
    PRIMARY KEY (id),
    FOREIGN KEY (author_id) REFERENCES authors(id),
    FOREIGN KEY (status_id) REFERENCES status(id)
);
--DROP table authors,countries,categories,books,status;