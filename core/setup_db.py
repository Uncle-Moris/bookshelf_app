import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database='bookshelf',
    user='postgres',
    password='Admin1'
)

cur = conn.cursor()

a = cur.execute("SELECT * FROM category")

print(a)
#cur.close()

conn.close()