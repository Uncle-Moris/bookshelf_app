from connections import ConnectionToDatabase


class Status:
    @staticmethod
    def add_new_status(name: str):
        ConnectionToDatabase.connection(
            'INSERT INTO public.status(name) values (%s)', (name, ))

    @staticmethod
    def list_of_all_status(status_name: str = None):
        if status_name is not None:
            return ConnectionToDatabase.select_all(
                f"SELECT * FROM public.categories WHERE name ilike '%{status_name}%' ORDER BY id",
                None)

        elif status_name is None:
            return ConnectionToDatabase.select_all("SELECT * FROM public.status "
                                                   "order by name asc "
                                                   "limit 10 ", None)


class StatusManaging:
    @staticmethod
    def sss():
        while True:
            print('categories managing panel')
            print("What you like do")
            print('')
            command = input(':')

            if command == 'Q':
                break

