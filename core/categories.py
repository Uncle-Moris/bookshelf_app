from time import sleep
from connections import ConnectionToDatabase


NL = '{\n}'


class Categories:
    @staticmethod
    def add_new_category(name: str):
        try:
            ConnectionToDatabase.connection(
                'INSERT INTO public.categories(name) values (%s)', (name, ))
        except:
            print(f"Category {name.upper()} already exist !")

    @staticmethod
    def list_of_all_similar_categories(category_name: str = None):
        if category_name is not None:
            return ConnectionToDatabase.select_all(
                f"SELECT name FROM public.categories WHERE name ilike '%{category_name}%'ORDER BY id",
                None)
        elif category_name is None:
            return ConnectionToDatabase.select_all("SELECT name FROM public.categories "
                                                   "order by name asc "
                                                   "limit 10 ", None)


class CategoriesManaging:
    COMMANDS = {"ADD": "Add new categories",
                "LS": "To list categories",
                "Q": "to go out from categories managing"}

    @staticmethod
    def run():
        """Allow to run status"""
        print('Categories managing panel')
        while True:
            command = input(
                f'What you like do ?\n\n'
                f'{str().join([f"{k} - {v}{NL}" for k, v in CategoriesManaging.COMMANDS.items()])}\n'
                f'Type command :').upper()

            if command == list(CategoriesManaging.COMMANDS.keys())[0]:
                new_category = input("Drop new categories name:")
                Categories.add_new_category(new_category)
                sleep(2)
                break


            elif command == 'LIST':
                for i in Categories.list_of_all_similar_categories():
                    print(i[0])
                    sleep(0.5)
                print('\n')

            elif command == 'SRCH':
                name = input("What are you looking for? :")
                for i in Categories.list_of_all_similar_categories(name):
                    print(i[0])
                print('\n')
            elif command == 'QUIT':
                break



