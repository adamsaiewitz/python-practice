players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

print("The first three items on this list are:")
print(players[0:3])

print("Three items from the middle of the list are:")
print(players[1:4])

print("The last three items in the list are:")
print(players[-3:])
