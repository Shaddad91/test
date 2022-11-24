import json

with open('player.json') as f:
    data = json.load(f)
print(data)