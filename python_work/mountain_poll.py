responses = {}

#Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    #Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    #Store the response in the dictionary:
    responses[name] = response

    #Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

#Polling is complete.  Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")


#7.8- 7.10
sandwich_orders = ['subway', 'pastrami', 'pastrami', 'runway', 'rainway', 'pastrami', 'sunway', 'noway']
finished_sandwiches = []
print("Sorry, our deli run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print("I mad your " + sandwich + " sandwich.\n")
    finished_sandwiches.append(sandwich)

print("List of sandwich made: ")
for finish in finished_sandwiches:
    print(finish)

####
places = {}
polling_active = True

while polling_active:
    name = input("Please enter your name: ")
    place = input("If you could visit one place in the world, where would you go?")

    places[name] = place

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("Result: \n")
for name, place in places.items():
    print(name + " would like to go " + place)