class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def newHi(self):
        print("Hi my name is", self.name,  "and I am", self.age, "years old.")

o1 = Player("Shaddad", 45)
# o1.newHi()
o1.age = 55
o1.newHi()