'''The objects in this file respond with the authors table'''
from datetime import datetime
from connections import ConnectionToDatabase


class Authors:
    def __init__(self,
            first_name:str,
            last_name: str,
            nationality: str):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality


class AuthorsManaging:

    @staticmethod
    def add_author():
        #while True:
        first_name = input('Enter the author\'s first name')
        last_name = input('Enter the author\'s last name')
        try:
            nationality = input('Enter counties name')
            natio = ConnectionToDatabase.select_all(
                f'SELECT shortcut '
                f'FROM countries '
                f'WHERE name ILIKE %s'
                f'LIMIT 1', (nationality,))
            print(natio[0][0])

        except print('')

        new_author = Authors(
            first_name=first_name,
            last_name=input('Enter the author\'s last` name'),
            nationality=input(),
        return new_author






print(AuthorsManaging.add_author())