import json

player = '{"Name": "Shaddad", "age": 31, "languages": ["English","Dhivehi"],"City":"Male"}'
player_dict = json.loads(player)
print(json.dumps(player_dict, indent = 4, sort_keys = True))
