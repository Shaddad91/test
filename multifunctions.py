class DoMath:

    def addition(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

first_object = DoMath()
print(first_object.addition(5,5))
print(first_object.subtraction(5,4))
print(first_object.multiplication(2,2))

second_object = DoMath()
print(second_object.addition(5,5))
print(second_object.subtraction(3,6))
print(second_object.multiplication(7,7))
