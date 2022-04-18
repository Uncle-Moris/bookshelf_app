import psycopg2


host = "localhost"
database = 'bookshelf'
user = 'postgres'
password = 'Admin1'

class Start:
    def __init__(self, host, database, user, password ):
        self.host = host
        self.database = database
        self.user = user
        self.password = password


    def get_conn(self):
        conn = psycopg2.connect(
            host = self.host,
            database = self.database,
            user = self.user,
            password = self.password
        )
        return conn
