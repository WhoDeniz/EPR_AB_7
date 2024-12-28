'''
invoice
'''

from tables import Table

class Invouce:
    def __init__(self, customer, total):
        self.customer = customer
        self.total = total

    def __str__(self):
        return f'Invoice from {self.table.tablenr} for {self.total}'