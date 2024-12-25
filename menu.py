'''
displays resaturant menu
'''
import csv


class Menu:

    def __init__(self):
        
        def menu_display():
            ''' reads csv file'''
            input_file = csv.DictReader(open("food.csv"),delimiter=";")
            print("--- Menu ---")
            for row in input_file:
                print(f"{row["name"]}, {row["type"]}, {row["category"]}, {row["price"]}€")


menu_display()
