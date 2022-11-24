class NewClass:
    def __init__(self):
        self.a = "Hello"

    def hi(self):
        return "Hi there!"
    
first_object = NewClass()

print(first_object.a)
print(first_object.hi())
