"""This module is responsible for status managing"""
from connections import ConnectionToDatabase


class Status:
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
                f"SELECT * FROM public.categories WHERE name ilike '%{status_name}%' ORDER BY id",
                None)

        #elif status_name is None:
        return ConnectionToDatabase.select_all("SELECT * FROM public.status "
                                                   "order by name asc"
                                                   , None)


class StatusManaging:
    COMMANDS = {"ADD": "To add new status",
                "LS": "To list status",
                "Q": "Go out from Status Managing"}

    @staticmethod
    def run():
        print('Status managing panel')
        while True:
            print("What you like do")
            print('Use ')
            command = input(':').upper()
            if command == 'ADD':
                pass

            elif command == 'ADD':
                pass

            elif command == 'Q':
                break
            else:
                pass
