__author__="8503197, Tas"
"""Müssen noch die Autoren hinzufügen"""

"""Müssen die Funktionen noch in classes umwandeln. Am besten in einzelnen .py Dateien machen weil ich das dezent verpeilt habe. Sollten am besten bis spätestens Donnerstag alles grob fertig haben damit wir genug Zeit 
   haben den Feinschliff noch hin zu bekommen"""

import csv


def menu_display():
    input_file = csv.DictReader(open("food.csv"),delimiter=";")
    print("--- Menu ---")
    for row in input_file:
        print(f"{row["name"]}, {row["typ"]}, {row["categorie"]}, {row["price"]}€")

"""Habe jetzt mit dem Ordering system angefangen. Der Anfang funktioniert ohne probleme, müssen jetzt nur daran 
   arbeiten das man beim Getränk auch nur ein Getränk bestellen kann und das selbe fürs Essen. Komme heute nicht dazu 
   aber vielleicht kann jemand von euch schon mal ein Blick drauf werfen. Tipp: Maybe mit einer for schleife prüfen 
   ob die Kategorie stimmt."""
def ordering():
    print("Hi Welcome to chili's!")
    while True:
        people = int(input("How many People are you? "))
        #Sollten eine Fail safe implementieren, falls der User ein String oder Float angibt
        if people <= 0:
            print("Oh sorry it seems there is a little problem. Could you repeat how many people you are?")
        else:
            print("Perfect! I will bring you to your table, come with me")


            print("That is our Menu")
            menu_display()

            drink = input("What do you want to drink?")


"""Habe hier erstmal ne Pause gemacht weil ich daran net arbeiten wollte. Vielleicht ist jemand motiviert um das 
   Dictionary in ein funktionierenden Zustand zu bekommen. Müssen noch das Prüfungssystem dafür implementieren. """
# def tisch(platz):
#
#
#     platz = {
#         "platz1": {
#             "anzahl": people,
#             "drink": drink,
#             "main": main,
#             "frei": True
#         },
#         "platz2": {
#             "anzahl": people,
#             "drink": drink,
#             "main": main,
#             "frei": True
#         },
#         "platz3": {
#             "anzahl": people,
#             "drink": drink,
#             "main": main,
#             "frei": True
#         },
#         "platz4": {
#             "anzahl": people,
#             "drink": drink,
#             "main": main,
#             "frei": True
#         },
#         "platz5": {
#             "anzahl": people,
#             "drink": drink,
#             "main": main,
#             "frei": True
#         },
#         "platz6": {
#             "anzahl": people,
#             "drink": drink,
#             "main": main,
#             "frei": True
#         }
#     }


ordering()














