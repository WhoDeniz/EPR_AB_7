'''
tisch
'''

import main

class Table:
    '''
    Table class to create table objects
    '''
    def __init__(self, table_number: int, table_status: bool, ):

        if table_number == 'None':
            pass
        else:
            self.table = table_number

        if table_status is False:
            self.satus = []
            print(f'Table {table_number} is free')

        else:
            self.status = table_status
            print(f'Table {table_number} is occupied')


T1 = Table(1, True)
T2 = Table(2, False)


for table in range():
    print('asd')
