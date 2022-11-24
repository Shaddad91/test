import json

print(json.dumps({"name":"Shaddad", "age": 31, "city": "Male"}))
print(json.dumps(["apple", "figs", "oranges", "bananas"]))
print(json.dumps(("apple", "figs")))
print(json.dumps("Hello there"))
print(json.dumps(31))
print(json.dumps(31.69))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))