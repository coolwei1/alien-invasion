dinner_list = []
dinner_list.append('wei han')
dinner_list.append('kai wen')
dinner_list.append('tian fatt')
print(dinner_list)

message = "\nI would like to invite you, " + dinner_list[0].title() + " ."
print(message)

message = "\nI would like to invite you, " + dinner_list[1].title() + " ."
print(message)

message = "\nI would like to invite you, " + dinner_list[2].title() + " ."
print(message)

print("\nWei Han unable to attend the dinner")

del dinner_list[0]
print(dinner_list)

dinner_list.insert(0, 'Yen Kang')
print(dinner_list)

message = "\n" + dinner_list[0] + ", I would like to invite you to dinner."
print(message)


print("\nHey guys, I'll invite more friends to the dinner as I found a bigger table!!")

dinner_list.insert(0, 'friend1')
dinner_list.insert(3, 'friend2')
dinner_list.append('friend3')

print(dinner_list)
print(len(dinner_list))

print("\nShit!!! I only can invite 2 friends !! Sorry guys!!!")

unable_to_invite = dinner_list.pop(0)
message = "Sorry " + unable_to_invite + " you fail."
print(message)

unable_to_invite = dinner_list.pop(2)
message = "Sorry " + unable_to_invite + " you fail."
print(message)

unable_to_invite = dinner_list.pop(0)
message = "Sorry " + unable_to_invite + " you fail."
print(message)

unable_to_invite = dinner_list.pop(0)
message = "Sorry " + unable_to_invite + " you fail."
print(message)

print(dinner_list)

message = "Hi, " + dinner_list[1] + " you are going to join my dinner !!"
print(message)

message = "Hi, " + dinner_list[0] + " you are going to join my dinner !!"
print(message)

del dinner_list[1]
del dinner_list[0]

print(dinner_list)

print(len(dinner_list))
