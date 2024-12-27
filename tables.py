'''
tisch
'''

from order import Order


class Table:
    '''
    Table class contains order of prople and status of the table
    '''
    def __init__(self, table_number: int, table_status: bool, order: Order):

        self.order = order

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

    def orderdetails(self):
        '''
        prints the order details
        '''
        print(f'Order details for table {self.table} are: ')
        self.order.ordering_drinks()
        self.order.ordering_food()
