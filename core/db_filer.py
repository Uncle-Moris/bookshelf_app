from requests import get
from connections import ConnectionToDatabase


def get_countries():
    return [[r['name']['common'], r['cca2']] for r in get('https://restcountries.com/v3.1/all').json()]


def filer():
    for i in get_countries():
        ConnectionToDatabase.connection(
            query="INSERT INTO countries (name ,shortcut)values (%s, %s)",
            values=(i[0], i[1]))


filer()

if __name__ == "__main__":

    def test_get_countries():
        result = get_countries()
        assert len(result) >= 9

