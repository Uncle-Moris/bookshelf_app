import psycopg2

from scripts import sql

host = "localhost"
database = 'bookshelf'
user = 'postgres'
password = 'Admin1'


conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)

cur = conn.cursor()

cur.execute(sql)


cur.close()
conn.commit()
conn.close()