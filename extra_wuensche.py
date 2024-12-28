'''
extra wishes for the costumers
'''

__author__ = "8503197, Tas"


class Extra_Wuensche:
    '''
    Extra_Wuensche class contains the extra wishes of the costumers
    '''
    def __init__(self):
        self.extra = []
        self.remove = []

    def plus(self):
        while True:
            more = input("Do you want to add(add) something for 1€ or "
                         "Do you want to remover(remove) something. "
                         "If u want to exit just say so.").strip().lower()

            if more == "add":
                lots = input("What do you want to add for 1€? ")
                self.extra.append(lots.strip().lower())
                continue
            elif more == "remove":
                expel = input("What do you want to remove? ")
                self.remove.append(expel.strip().lower())
                continue
            else:
                print("If you need something just call me!")
                break

    def get_extra(self):
        return self.extra

    def get_removed(self):
        return self.remove
