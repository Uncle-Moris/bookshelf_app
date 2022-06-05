'''The objects in this file respond with the authors table'''
from datetime import datetime
from connections import ConnectionToDatabase
from time import sleep

NL = '\n'

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

        ConnectionToDatabase.connection(
            'INSERT INTO  authors (first_name, last_name, nationality)'
            'values (%s, %s, %s)',
            (new_author.first_name,
             new_author.last_name,
             new_author.nationality)
        )



    @staticmethod
    def get_author():
        fullname = input("Who you looking for ?")
        fullname = fullname.split(' ')
        results = ConnectionToDatabase.select_all(
            f"SELECT * "
            f"FROM authors "
            f"where first_name "
            f"ilike '%{fullname[0]}%' "
            f"and last_name "
            f"ilike '%{fullname[1]}%'",
            None)
        return print(results)


class AuthorsManaging:
    """Class responsible for driving actions on authors"""

    COMMANDS = {"ADD": "To add new author",
                "SRCH": "To search author by name",
                "Q": "Go out from Status Managing"}

    @staticmethod
    def run():
        """Allow to run managing"""
        print('Authors managing panel')
        while True:
            command = input(
                f'What you like do ?\n\n'
                f'{"".join([f"{k} - {v}{NL}" for k, v in AuthorsManaging.COMMANDS.items()])}\n'
                f'Type command :').upper()
            if command == list(AuthorsManaging.COMMANDS.keys())[0]:
                Authors.add_author()

            elif command == list(AuthorsManaging.COMMANDS.keys())[1]:
                Authors.get_author()

            elif command == list(AuthorsManaging.COMMANDS.keys())[2]:
                break

            else:
                print('Wrong command, try again.\n ')
                sleep(1.5)

if __name__ == '__main__':
    AuthorsManaging.run()