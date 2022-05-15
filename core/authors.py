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

    def add_author(self):
        ConnectionToDatabase(
            f"INSERT INTO authors (first_name, last_name, nationality, date_of_birt, date_of_die)"
            "values ('s%', 's%','s%', 's%', 's%')",
            (self.first_name,
             self.last_name,
             self.nationality,
             self.date_of_birt,
             self.date_of_die
             ))

    @staticmethod
    def get_authors(self):
        pass



class AuthorsManaging:
    pass




