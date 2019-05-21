import re


def outer(print_name):
    def inner(self):
        if re.match("^[pP].*a$", self.name):
            return print_name(self)
        else:
            print("The entered name is not matching!!!")
    return inner

class printing():
    def __init__(self, name):
        self.name = name
    @outer
    def print_name(self):
        print("The name is matching", self.name)
p = printing("Poorvika")
p.print_name()

