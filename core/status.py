"""This module is responsible for status managing"""
from time import sleep
from connections import ConnectionToDatabase

NL = '\n'


class Status:
    """Class responsible for managing status table in database"""
    @staticmethod
    def add_new_status(name: str):
        """Method responsible for adding new status"""
        ConnectionToDatabase.connection(
            'INSERT INTO public.status(name) values (%s)', (name, ))

    @staticmethod
    def list_of_all_status(status_name: str = None):
        """This method is responsible for displaying the available results"""
        if status_name is not None:
            return ConnectionToDatabase.select_all(
                f"SELECT name FROM public.status WHERE name ilike '%{status_name}%' ORDER BY id",
                None)
        return ConnectionToDatabase.select_all("SELECT name FROM public.status "
                                               "order by name asc", None)


class StatusManaging:
    """Class responsible for driving actions on status"""

    COMMANDS = {"ADD": "To add new status",
                "LS": "To list status",
                "SRCH": "To search by name",
                "Q": "Go out from Status Managing"}

    @staticmethod
    def run():
        """Allow to run managing"""
        print('Status managing panel')
        while True:
            command = input(
                f'What you like do ?\n\n'
                f'{"".join([f"{k} - {v}{NL}" for k, v in StatusManaging.COMMANDS.items()])}\n'
                f'Type command :').upper()

            if command == list(StatusManaging.COMMANDS.keys())[0]:
                new_status_name = input("Defined a new status name\n: ")
                Status.add_new_status(new_status_name)

            elif command == list(StatusManaging.COMMANDS.keys())[2]:
                status_name = input("What are you looking for ? \n:")
                for i in Status.list_of_all_status(status_name):
                    print(i[0])
                    sleep(0.5)
                sleep(3)
                print('\n')

            elif command == list(StatusManaging.COMMANDS.keys())[1]:
                for i in Status.list_of_all_status():
                    print(i[0])
                    sleep(0.5)
                sleep(3)
                print('\n')

            elif command == list(StatusManaging.COMMANDS.keys())[3]:
                break

            else:
                pass
