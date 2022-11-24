players = {"Messi":10, "Salah":11,"Firmino":9}
y = input("Whose jersey number do you want to check? ")
#This will show 'None' if key is not found, kinda better than the one below.
print(players.get(y))

#Will show a KeyError
# print(players[y]) 