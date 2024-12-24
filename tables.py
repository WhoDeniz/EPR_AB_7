'''
tisch
'''

from typing import Dict
from AB 07 Gruppe import ordering


tables = {}


def add_table(tables: Dict, location: str, occupancy: bool, attributes: Dict):
    '''
    adds table with number of people, drink, main and says if full
    '''

    if location not in tables:
        tables[location] = {}
    tables[location][occupancy] = attributes



def count():
    n = 1
    while n <= 6:
        print(f'table {n}')
        n = n + 1




add_table(tables, count(), False, {'Anzahl': people/4})



def tisch(platz):


    platz = {
         "platz1": {
             "anzahl": people,
             "drink": drink,
             "main": main,
             "frei": True
         },
         "platz2": {
             "anzahl": people,
             "drink": drink,
             "main": main,
             "frei": True
         },
         "platz3": {
             "anzahl": people,
             "drink": drink,
             "main": main,
             "frei": True
         },
         "platz4": {
             "anzahl": people,
             "drink": drink,
             "main": main,
             "frei": True
         },
         "platz5": {
             "anzahl": people,
             "drink": drink,
             "main": main,
             "frei": True
         },
         "platz6": {
             "anzahl": people,
             "drink": drink,
             "main": main,
             "frei": True
         }
     }
'''


