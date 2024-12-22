__author__="8503197, Tas"

import csv

class Menu:

    def __init__(self, ):


    def menu_display(self):
        input_file = csv.DictReader(open("food.csv"), delimiter=";")
        print("--- Menu ---")
        for row in input_file:
            print(f"{row["name"]}, {row["typ"]}, {row["categorie"]}, {row["price"]}€")