import json
#adding json
player1 = '{"name":"Shaddad", "age": 31, "city": "Male"}'
#parse
x = json.loads(player1)
print(x["city"]) 