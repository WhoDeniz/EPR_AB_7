'''
tzuij
'''

import menu


def ordering():
    print("Hi Welcome to chili's!")
    while True:
        people = int(input("How many People are you? "))
        # Sollten eine Fail safe implementieren, falls der User ein String oder Float angibt
        if people <= 0:
            print("Oh sorry it seems there is a little problem. Could you repeat how many people you are?")
        else:
            print("Perfect! I will bring you to your table, come with me")


            print("That is our Menu")
            menu.menu_display()

            drink = input("What do you want to drink?")
        return people


"""Habe hier erstmal ne Pause gemacht weil ich daran net arbeiten wollte. Vielleicht ist jemand motiviert um das 
   Dictionary in ein funktionierenden Zustand zu bekommen. Müssen noch das Prüfungssystem dafür implementieren. """


ordering()
