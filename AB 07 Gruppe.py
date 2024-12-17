__author__="8503197, Tas"

import csv


def menu_display():
    input_file = csv.DictReader(open("food.csv"),delimiter=";")
    print("--- Menu ---")
    for row in input_file:
        print(f"{row["name"]}, {row["typ"]}, {row["categorie"]}, {row["price"]}€")


def tisch(platz):

    people = input("")
    drink = input("")
    main = input("")

    platz = {
        "platz1": {
            "anzahl": people,
            "drink": drink,
            "main": main,
            "frei": True
        },
        "platz2": {
            "anzahl": people,
            "drink": drink,
            "main": main,
            "frei": True
        },
        "platz3": {
            "anzahl": people,
            "drink": drink,
            "main": main,
            "frei": True
        },
        "platz4": {
            "anzahl": people,
            "drink": drink,
            "main": main,
            "frei": True
        },
        "platz5": {
            "anzahl": people,
            "drink": drink,
            "main": main,
            "frei": True
        },
        "platz6": {
            "anzahl": people,
            "drink": drink,
            "main": main,
            "frei": True
        }
    }

def check_if_true(platz):















