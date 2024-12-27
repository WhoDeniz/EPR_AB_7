__author__="8503197, Tas"
from ordering_system import Order
from menu import Menu
from extra_wuensche import Extra_Wuensche


class Uebersicht:
    def __init__(self):

        self.menu = Menu("food.csv")
        self.menu.load_menu()

        self.extra_wuensche = Extra_Wuensche()

        self.order = Order("food.csv")


    def anzeige(self):

        while True:
            print("\n1.Bestellung aufnehmen")
            print("2.Tisch übersicht") #Tisch System
            print("3.Extra Wünsche")
            print("4.Menü anzeigen")
            print("5.Rechnung ausdrucken")
            print("6.Exit")


            auswahl = input("\nGeben Sie bitte die gewünschte Funktion ein(1-6):")

            if auswahl == "1":
                self.order.bestellung_aufnehmen()
            elif auswahl == "2":#GOTO Tisch system fertig machen
                pass
            elif auswahl == "3":
                 self.extra_wuensche.plus()
            elif auswahl == "4":
                 self.menu.menu_display() #Menue anzeigen lassen
            elif auswahl == "5": #GOT Rechnung System fertig machen
                pass
            elif auswahl == "6":
                print("Goodbye!!!")
                exit()
            else:
                print("Ungültige Auswahl. Bitte wählen Sie eine Zahl zwischen 1 und 6.")

if __name__ == "__main__":
    uebersicht = Uebersicht()
    uebersicht.anzeige()



