import authors
import books
import categories
import status

NL = '\n'


class Driver:
    COMMANDS = {"Authors": "Entry to Authors panel",
                "Books": "Entry to Books panel",
                "Categories": "Entry to Categories panel",
                "Status": "Entry to Status panel",
                "Quit": "Close the program"}

    @staticmethod
    def run():
        """Allow to managing program"""
        print('Status managing panel')
        while True:

            command = input(
                f'What you like do ?\n\n'
                f'{str().join([f"{k} - {v}{NL}" for k, v in Driver.COMMANDS.items()])}\n'
                f'Type command :')

            if command == list(Driver.COMMANDS.keys())[0]:
                """To fill when Authors.py will be ready"""
                pass
            elif command == list(Driver.COMMANDS.keys())[1]:
                """To fill when Books.py will be ready"""
                pass
            elif command == list(Driver.COMMANDS.keys())[2]:
                """To fill when Categories.py will be ready"""
                categories.CategoriesManaging.run()
            elif command == list(Driver.COMMANDS.keys())[3]:
                """To fill when Status.py will be ready"""
                status.StatusManaging.run()

            elif command == list(Driver.COMMANDS.keys())[4]:
                break; quit()

            else:
                print("You probably use incorrect command and, try again.")

if __name__ == '__main__':
    Driver.run()