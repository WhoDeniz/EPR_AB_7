'''
invoice
'''

__author__ = "8503197, Tas, 8566858, Socol"


from tables import Table


class Invoice:
    '''
    Invoice class contains the invoice details
    '''
    def __init__(self, table: Table):
        self.table = table
        self.customer = f'Table {table.tablenr}'
        self.total = self.calculate_total()

    def calculate_total(self):
        '''
        calculates the total amount of the order
        '''
        total = 0
        menu = self.table.order.menu  # Access the menu from the order

        for drink in self.table.order.tabledrink:
            total += menu.get_price(drink)

        for food in self.table.order.tablefood:
            total += menu.get_price(food)

        # Assuming extra wishes are stored in a list called extra_wishes
        for wish in self.table.order.extra_wuensche.get_extra():
            total += 1

        return total

    def __str__(self):
        return f'Invoice from {self.customer} for {self.total}€'


# Example usage
if __name__ == "__main__":
    from ordering_system import Order

    order = Order(menu_file="food.csv")
    order.tabledrink = ['cola', 'beer']
    order.tablefood = ['burger', 'pizza']
    order.extra_wuensche.extra = ['extra cheese', 'extra ketchup']

    table = Table(table_status=True, order=order)
    invoice = Invoice(table)
    print(invoice)
