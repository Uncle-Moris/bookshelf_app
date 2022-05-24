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

    @staticmethod
    def add_author():
        try:
            first_name = input('Enter the author\'s first name')
            last_name = input('Enter the author\'s last name')

            nationality = input('Enter counties name')
            natio = ConnectionToDatabase.select_all(
                f'SELECT shortcut '
                f'FROM countries '
                f'WHERE name ILIKE %s'
                f'LIMIT 1', (nationality,))

        except Exception:
            print('You used some bad data')

        new_author = Authors(
            first_name=first_name,
            last_name=last_name,
            nationality=natio[0][0])
        return new_author

    @staticmethod
    def get_author():
        fullname = input("Who you looking for ?")
        fullname = fullname.split(' ')
        return ConnectionToDatabase.connection("SELECT *"
                                               " FROM authors "
                                               "where "
                                               "first_name ilike %s "
                                               "and"
                                               " last_name ilike %s",
                                        (fullname[0], fullname[1]))


class AuthorsManaging:
    COMMANDS = {"ADD": "To add new author",
                "SRCH": "To search author by name",
                "Q": "Go out from Status Managing"}

    @staticmethod
    def run():
        """Allow to run managing"""
        print('Authors managing panel')





