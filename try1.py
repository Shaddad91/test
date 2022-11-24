try:
    print(a)
except NameError:
    print("Variable is not defined")
except:
    print('This is an exception')