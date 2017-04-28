players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())

message = "\nThree item from the middle of the list are:"
print(message)
print(players[1:4])

message = "\nThe last three items in the list are:"
print(message)
print(players[2:])
