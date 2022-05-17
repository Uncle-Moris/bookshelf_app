from authors import Authors
from datetime import datetime

#a=date#time.date(1998, 1, 2)
#b=datetime.date(1998, 1, 2)

test1 = Authors(first_name='Jan',
                last_name='Wojtyła',
                nationality= 'PL',
                date_of_birt=(1998, 1, 2),
                date_of_die=(1998, 1, 2))

print(test1.date_of_die,test1.date_of_birt)