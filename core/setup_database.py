from connections import ConnectionToDatabase

sql = open("../migrations/initial_db_script.sql").read()


if __name__ == "__main__":

    stat_up_db = ConnectionToDatabase
    stat_up_db.connection(sql)