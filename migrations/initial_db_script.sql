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
    --details JSONB, (move dates of birt and die in to json format)
    nationality VARCHAR,
        PRIMARY KEY (id),
        FOREIGN KEY (nationality) REFERENCES countries(shortcut) ON UPDATE CASCADE
);
--Books--
CREATE TABLE IF NOT EXISTS books(
    id SERIAL,
    title VARCHAR,
    --details JSONB,
    author_id INT NOT NULL,
    status_id INTEGER NOT NULL,
    published_at DATE,
        PRIMARY KEY (id),
        FOREIGN KEY (author_id)
            REFERENCES authors(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE ,
        FOREIGN KEY (status_id)
            REFERENCES status(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE
);
--DROP table authors,countries,categories,books,status;