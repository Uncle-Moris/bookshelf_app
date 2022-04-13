CREATE TABLE IF NOT EXISTS category(
    id SERIAL PRIMARY KEY,
    name  VARCHAR(250) UNIQUE,
    created_at TIMESTAMP --Add some autoincrement wey to fill values--
);
