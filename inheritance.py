class Anyone:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def display(self):
        print(self.firstname, self.lastname)
# myObj = Anyone("Shaddad", "Haleem")
# myObj.display()
class Player(Anyone):
    pass
myObj = Player("Shaddad", "Haleem")
myObj.display()