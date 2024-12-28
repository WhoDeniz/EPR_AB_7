'''
tisch
'''

from ordering_system import Order


class Table:
    '''
    Table class contains order of prople and status of the table
    '''
    last_tablenr = 0

    def __init__(self, table_status: bool, order: Order):
        Table.last_tablenr += 1
        self.tablenr = Table.last_tablenr

        self.order = order

        if table_status is False:
            self.status = []
            print(f'Table {self.tablenr} is free')

        else:
            self.status = table_status
            print(f'Table {self.tablenr} is occupied')

    def orderdetails(self):
        '''
        prints the order details
        '''
        print(f'Order details for table {self.tablenr} are: ')
        if not self.order.tabledrink and not self.order.tablefood:
            print('No order yet')
        else:
            print(f'Order number: {self.order.ordernr}')
            print(f'Drinks: {self.order.get_drinks_str()}')
            print(f'Food: {self.order.get_food_str()}')




# Example usage
if __name__ == "__main__":
    order1 = Order(menu_file="food.csv")
    order1.ordering_drinks()

    table1 = Table(table_status=True, order=order1)
    table1.orderdetails()
    