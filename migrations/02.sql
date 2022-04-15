--Countries--

CREATE TABLE IF NOT EXISTS countries(
    id INTEGER NOT NULL ,
    name VARCHAR(255) UNIQUE,
    shortcut VARCHAR(2) UNIQUE,
    PRIMARY KEY (id)
);

--Authors--
CREATE TABLE IF NOT EXISTS authors(
    id INTEGER NOT NULL ,
    full_name VARCHAR UNIQUE,
    nationality INTEGER,
    date_of_birt DATE NOT NULL,
    date_of_die DATE,
    PRIMARY KEY (id),
    FOREIGN KEY (nationality)
        REFERENCES categories(id)
);

--Categories--

CREATE TABLE IF NOT EXISTS  categories(
    id INTEGER,
    name VARCHAR,
    PRIMARY KEY (id)
);

--Status--
CREATE TABLE IF NOT EXISTS  status(
    id INTEGER,
    name VARCHAR,
    PRIMARY KEY (id)
);

--Books--
CREATE TABLE IF NOT EXISTS books(
    id INTEGER,
    name VARCHAR,
    --author_id INTEGER NOT NULL,
    author_name varchar,
    status_id INTEGER NOT NULL,
    published_at DATE,
    PRIMARY KEY (id),
    --FOREIGN KEY (author_id) REFERENCES authors(id),
    FOREIGN KEY (author_name) REFERENCES authors(full_name),
    FOREIGN KEY (status_id) REFERENCES status(id)
);