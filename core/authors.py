'''The objects in this file respond with the authors table'''
from datetime import datetime
from connections import ConnectionToDatabase


class Authors:
    def __init__(self,
            first_name:str,
            last_name: str,
            nationality: str,
            date_of_birt: datetime.date,
            date_of_die: datetime.date):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.date_of_birt = date_of_birt
        self.date_of_die = date_of_die






'''
        ConnectionToDatabase(
            f"INSERT INTO authors (first_name, last_name, nationality, date_of_birt, date_of_die)"
            "values ('s%', 's%','s%', 's%', 's%')",
            (self.first_name,
             self.last_name,
             self.nationality,
             self.date_of_birt,
             self.date_of_die
             ))
'''

#    @staticmethod
#    def get_authors(self):
#        pass



class AuthorsManaging:

    @staticmethod
    def add_author():
        #while True:
        first_name = input('Enter the author\'s first name')
        last_name = input('Enter the author\'s last name')
        try:

            nationality = ConnectionToDatabase()
            pass

        date_of_birt = input(4)
        date_of_die = input(5)

        new_author = Authors(
            first_name=first_name,
            last_name=input('Enter the author\'s last` name'),
            nationality=input(),
            date_of_birt=input(4),
            date_of_die=input(5))
        return new_author






print(AuthorsManaging.add_author())