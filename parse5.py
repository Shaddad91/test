import json

player1 = {
    "name": "Shaddad",
    "age": 31,
    "languages": ["English", "Dhivehi"],
    "city": "Male"
}

with open ("player1.txt", "w") as json_file:
    json.dump(player1, json_file)