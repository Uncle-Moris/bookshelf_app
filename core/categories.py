from connections import ConnectionToDatabase


class Categories:
    @staticmethod
    def add_new_category(name: str):
        ConnectionToDatabase.connection(
            'INSERT INTO public.categories(name) values (%s)', (name, ))

    @staticmethod
    def list_of_all_similar_categories(category_name: str = None):
        if category_name is not None:
            return ConnectionToDatabase.select_all(
                f"SELECT * FROM public.categories WHERE name ilike '%{category_name}%'",
                None)
        elif category_name is None:
            return ConnectionToDatabase.select_all("SELECT * FROM public.categories "
                                                   "order by name asc "
                                                   "limit 10 ", None)


class Categories_Managing:
    @staticmethod
    def sss():
        while True:
            print('categories managing panel')
            print("What you like do")
            print('')
            command = input(':')
            if command == 'Q':
                break

