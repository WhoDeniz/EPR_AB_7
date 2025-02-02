__author__="8503197, Tas"

import csv

class Menu:
    """
    Die Class wird initialisiert
    """
    def __init__(self, input_file):
        self.input_file = input_file #CSV Datei
        self.items = [] #Alle Items
        self.drinks = [] #Nur Drinks
        self.food = [] #Nur Essen

    def load_menu(self):
        """
        Mit der with open sequenz stellen wir sicher, dass die Datei geöffnet wird. Die newline Stelle sorgt dafür
        das der Zeilenumbruch korrekt stattfindet und die encoding Sequenz stellt sicher, dass die korrekten zeichen
        gelesen werden. Dabei wird mit dem with die Datei sicher geöffnet und geschlossen. PS: Das hat zu lange
        gebraucht um zu funktionieren....
        """
        with open(self.input_file, newline="", encoding="utf-8") as csvfile:
            """
            Mit dem csv.DictReader wird die CSV Datei gelesen und in der Variabel gespeichert. Damit aber nicht 
            alles in einer Reihe ausgegeben wird ist der delimiter da. Danke an den einen Random typen der uns geholfen 
            hat
            """
            input_file = csv.DictReader(csvfile, delimiter=";")
            for row in input_file:
                self.items.append(row)
                if row["typ"].lower() == "drink":
                    self.drinks.append(row["name"].strip().lower())
                if "main" in row["typ"].lower():
                    self.food.append(row["name"].strip().lower())


    def menu_display(self):
            """
            Printed die einzelnen Kolumnen und gibt damit das ganze Menü aus
            """
            print("--- Menu ---")
            for row in self.items:
                print(f"{row["name"]}, {row["typ"]}, {row["categorie"]}, {row["price"]}€")

    def get_food(self):
        return self.food #Damit die Main gerichte auch in die Liste gelangen und im ordering System genutzt
                         # werden können

    def get_drinks(self):
        return self.drinks #Same thing hier

""""
"Wird nur direkt ausgeführt wenn die Datei als Skript gestartet wird. Musste so implementiert damit wir trotzdem datei
testen können und es nicht in anderen Dateien direkt ausgeführt wird.
"""
if __name__ == "__main__":
    menu = Menu("food.csv")
    menu.load_menu()
    menu.menu_display()





