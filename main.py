from menu import Menu
from order import Order
from tables import Table


menu = Menu("food.csv")
menu.load_menu()
menu.menu_display()


order = Order("food.csv")
order.thy_table()
order.ordering_drinks()
order.ordering_food()


T1 = Table(1, True, [Order.ordering_drinks, Order.ordering_food])

T1.orderdetails()
