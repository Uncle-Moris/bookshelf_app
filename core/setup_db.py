import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database='bookshelf',
    user='postgres',
    password='Admin1'
)

cur = conn.cursor()

a = cur.execute(
    """CREATE TABLE IF NOT EXISTS authors(
    id SERIAL PRIMARY KEY, 
    name varchar,
    year_of_birth DATE)""")


cur.close()
conn.commit()
conn.close()