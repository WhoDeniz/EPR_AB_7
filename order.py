'''
order per table
'''
__author__ = "8503197, Tas"

from menu import Menu


class Order:
    '''
    Order class contains the order of the people
    '''

    def __init__(self, menu_file):
        """
        Hier wird die Order class initialisiert
        """
        self.menu = Menu(menu_file)    # Wir laden die CSV file in die Variabel self.menu.
        self.menu.load_menu()
        self.drinks = self.menu.get_drinks()    # Die Liste mit den Getränken wird hier abgespeichert
        self.food = self.menu.get_food()    # Dir Liste mit dem Essen wir hier abgespeichert

    def thy_table(self):
        """
        Mit while True wird die Sequenz wiederholt bis eine Valide Zahl
        eingegeben wird. Wenn das Geschieht verlässt man die Schleife. Alls
        fail safe haben wir ein except ValueError eingebaut. Verhindert, dass
        das Programm abschmiert, wenn man keine Zahl eingibt.
        """
        while True:
            try:
                people = int(input("Hi Welcome to chili's!How many people are you? "))    # Vine times
                if people <= 0:    # Weniger als ein Gast zu bedienen ist halt auch schwer
                    people = int(input("Oh sorry it seems there is a little problem. Could you repeat how many "
                                       "people you are?"))
                    return people    # Die (hoffentlich) Valide Zahl wird zurückgegeben.

                else:
                    print("Perfect! I will bring you to your table, come with me.\n--Here is our whole menu!--")
                    self.menu.menu_display()    # Aufrufen des Menüs, wenn eine Valide Zahl eingegeben wurde. Import aus menu.py
                    break    # Verässt die Schleif
            except ValueError:
                print("Oh my, what happened there. Lets try it again as if nothing happened, alright?")    # Erwähnter fail safe

    def ordering_drinks(self):
        """
        Abfrage nach Getränken. So implementiert damit auch nur Getränke eingegeben werden können. Das hat mir zu viele
        kopfschmerzen bereitet, mehr als ich jemals erwarten konnte.
        """
        while True:    # Solange es true ist, wird die Sequenz wiederholt.
            drink = input("What do you wanna drink?").strip().lower()   # Das.strip() hat mir kostbare Lebensjahre geraubt.
                                                                        # Erst dann hat es funktioniert. In diesem
                                                                        # Restaurant muss man mindestens ein Getränk
                                                                        # bestellen. Wir sind böse idc.
            if drink in self.drinks:
                again = input(f"Great here is your {drink}, do you want something else(yes/no)?: ").strip().lower()
                if again == "yes":    # Möglichkeit mehrere Sachen zu bestellen
                    continue
                else:
                    print("Perfect! Enjoy your drink! I will be back if u want to order food. ")
                    break    # Damit wir nicht in einer dauerschleife gefangen sind
            else:
                print("Oh sorry we dont have that in our menu, would you like something different?")
                print("Those are our drinks", ",".join(self.drinks))    # Eine Auflistung der Getränke damit man nicht die
                                                                        # ganze Zeit hochgehen muss

    def ordering_food(self):
        """
        Nach Essen wird abgefragt
        """
        while True:
            food = input("What do you wanna eat?").strip().lower()

            if food in self.food:
                again = input(f"Great here is your {food}, do you want something else(yes/no)?: ").strip().lower()
                if again == "yes":
                    continue
                else:
                    print("Alrighty! Enjoy your food. If u need something just call me.")
                    break
            else:
                print("Oh sorry we dont have that in our menu, would you like something different?")
                print("Those are our Main dishes", ",".join(self.food))    # Alles genauso wie bei den drinks


if __name__ == "__main__":
    order = Order("food.csv")
    order.thy_table()
    order.ordering_drinks()
    order.ordering_food()
