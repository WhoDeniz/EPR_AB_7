'''
UI
'''

__author__ = "8503197, Tas; 8566858, Socol"

from ordering_system import Order
from menu import Menu
from extra_wuensche import Extra_Wuensche
from tables import Table
from invoice import Invoice


class Uebersicht:
    def __init__(self):

        self.menu = Menu("food.csv")
        self.menu.load_menu()

        self.extra_wuensche = Extra_Wuensche()

        self.tables = []

    def anzeige(self):

        while True:
            print("\n1.Bestellung aufnehmen")
            print("2.Tisch übersicht")  # Tisch System
            print("3.Extra Wünsche")
            print("4.Menü anzeigen")
            print("5.Rechnung ausdrucken")
            print("6.Exit")

            auswahl = input("\nGeben Sie bitte die gewünschte Funktion ein(1-6): ")

            if auswahl == "1":
                order = Order("food.csv")
                order.bestellung_aufnehmen()
                table = Table(True, order)
                self.tables.append(table)
                print(f"New table {table.tablenr} added with order number {order.ordernr}")
            elif auswahl == "2":
                for table in self.tables:
                    table.orderdetails()
            elif auswahl == "3":
                self.extra_wuensche.plus()
            elif auswahl == "4":
                self.menu.menu_display()  # Menue anzeigen lassen
            elif auswahl == "5":  # GOT Rechnung System fertig machen
                table_number = int(input("Enter the table number for the invoice: "))
                table = next((t for t in self.tables if t.tablenr == table_number), None)
                if table:
                    invoice = Invoice(table)
                    print(invoice)
                else:
                    print(f"No table found with number {table_number}")
            elif auswahl == "6":
                print("Goodbye!!!")
                exit()
            else:
                print("Ungültige Auswahl. Bitte wählen Sie eine Zahl zwischen 1 und 6.")


if __name__ == "__main__":
    uebersicht = Uebersicht()
    uebersicht.anzeige()
