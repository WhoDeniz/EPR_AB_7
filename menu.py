'''
displays resaturant menu
'''
import csv


class Menu:
    """Die Class wird initialisiert"""
    def __init__(self, input_file):
        self.input_file = input_file

    def menu_display(self):
        """"Mit der with open sequenz stellen wir sicher, dass die Datei geöffnet wird. Die newline Stelle sorgt dafür
        das der Zeilenumbruch korrekt stattfindet und die encoding Sequenz stellt sicher, dass die korrekten zeichen
        gelesen werden. Dabei wird mit dem with die Datei sicher geöffnet und geschlossen. PS: Das hat zu lange
        gebraucht um zu funktionieren...."""
        with open(self.input_file, newline="", encoding="utf-8") as csvfile:
            """Mit dem csv.DictReader wird die CSV Datei gelesen und in der Variabel gespeichert. Damit aber nicht 
            alles in einer Reihe ausgegeben wird ist der delimiter da. Danke an den einen Random typen der uns geholfen 
            hat"""
            input_file = csv.DictReader(csvfile, delimiter=";")
            """Printed die einzelnen Kolumnen"""
            print("--- Menu ---")
            for row in input_file:
                print(f"{row["name"]}, {row["typ"]}, {row["categorie"]}, {row["price"]}€")

"""Wird nur direkt ausgeführt wenn die Datei als Skript gestartet wird. Musste so implementiert damit wir trotzdem datei
testen können und es nicht in anderen Dateien direkt ausgeführt wird. """
if __name__ == "__main__":
    menu = Menu("food.csv")
    menu.menu_display()
