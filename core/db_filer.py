from requests import get
from setup_db import DB_Comunication


def get_countries():
    return [[r['name']['common'], r['cca2']] for r in get('https://restcountries.com/v3.1/all').json()]


for i in get_countries():
    DB_Comunication.connection(f'INSERT INTO public.countries (name, shortcut) values ({str(i[0])} ,{str(i[1])})')


