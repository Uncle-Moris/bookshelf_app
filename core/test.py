#from authors import Authors
from datetime import datetime
from connections import ConnectionToDatabase

nationality = input('Enter counties name')
natio = ConnectionToDatabase.select_all(
                    f'SELECT shortcut '
                    f'FROM countries '
                    f'WHERE name ILIKE %s'
                    f'LIMIT 1', (nationality, ))
print(natio[0][0])