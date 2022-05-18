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

class AuthorsManaging:

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
            nationality= natio[0][0])

        ConnectionToDatabase.connection('INSERT INTO public.authors(first_name,last_name,nationality) values(%s,%s,%s)',(
                                                   new_author.first_name,
                                                    new_author.last_name,
                                                    new_author.nationality))
        print("its works !!!!")



test = AuthorsManaging().add_author()

