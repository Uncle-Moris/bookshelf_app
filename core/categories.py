from connections import ConnectionToDatabase


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
    @staticmethod
    def run():
        while True:
            print('categories managing panel')
            print("QUIT - Left Categories Managing\n"
                  "LIST - Get list of all categories\n"
                  "ADD  - Add new categories \n"
                  "SRCH - Get simular categories list")
            command = input('What you like do? Type command :')
            if command == 'ADD':
                new_category = input("Drop new categories name:")
                Categories.add_new_category(new_category)


            elif command == 'LIST':
                for i in Categories.list_of_all_similar_categories():
                    print(i[0])
            elif command == 'SRCH':
                name = input("What are you looking for? :")
                for i in Categories.list_of_all_similar_categories(name):
                    print(i[0])
                print('\n')
            elif command == 'QUIT':
                break;break
            else:
                pass



CategoriesManaging.run()
