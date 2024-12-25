'''
displays resaturant menu
'''
import csv


def menu_display():
    ''' reads csv file'''
    input_file = csv.DictReader(open("food.csv"),delimiter=";")
    print("\n\n--- Menu ---\n")
    for row in input_file:
        print(f"{row["name"]}, {row["type"]}, {row["category"]}, {row["price"]}€")


# TEST menu_display()
