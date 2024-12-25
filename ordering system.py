__author__="8503197, Tas"

from menu import Menu

class Order:

    def __init__(self, people, menu_file):
        self.people = people
        self.menu = Menu(menu_file)

    def ordering(self):
        while self.people <= 0:
            print("Oh sorry it seems there is a little problem. Could you repeat how many people you are?")
            self.people = int(input("How many people are you? "))

        print("Perfect! I will bring you to your table, come with me.")


        print("That is our Menu: ")
        self.menu.menu_display()

        drink = input("\nWhat do you want to drink?")
        #while True:
        if "drink" == "categorie":
            print("Oh sorry you need to choose a drink")
            drink = input("\nWhat do you want to drink?")
        else:
            print(f"Great Choice! We will get your {drink} ready.")

print("Hi Welcome to chili's!")
people = int(input("How many people are you? "))

order = Order(people, "food.csv")
order.ordering()