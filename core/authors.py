'''The objects in this file respond with the authors table'''
from datetime import datetime
from connections import ConnectionToDatabase


class Authors:
    def __init__(self,
            first_name:str,
            last_name: str,
            nationality: str,
            date_of_birt: datetime,
            date_of_die: datetime):

        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.date_of_birt = date_of_birt
        self.date_of_die = date_of_die

    def add_author(self):
        ConnectionToDatabase(
            "INSERT INTO authors () values ()",
            (self.first_name,
             self.last_name,
             self.nationality,
             self.date_of_birt,
             self.date_of_die
             ))
