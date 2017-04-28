users = ['admin', 'coolwei1', 'dawn2dusk', 'frosmoaoif', 'wtf']

for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see status report?\n")
    else:
        print("Hello " + user + ",thank you for loging in again.\n")
#check if this is empty list
else:
    print("We need to find some users!!")





current_users = ['cooLwei1', 'cOolwei', 'abc', 'wtf', 'SHit']
current_users_list = []
new_users = ['coolWei', 'joHor', 'Najib', 'rOcket', 'sHIt']
new_users_list = []

for current_user in current_users:
    current_users_list.append(current_user.lower())

print(current_users_list)

for new_user in new_users:
    new_users_list.append(new_user.lower())

print(new_users_list)

for new_user in new_users_list:
    if new_user in current_users_list:
        print("This username not available")
    else:
        print("You can use this username")

numbers_list = ['1', '2', '3', '4', '5', '6', '9']

for number_list in numbers_list:
    if '1' in number_list:
        print('\n1st')
    elif '2' in number_list:
        print('\n2nd')
    elif '3' in number_list:
        print('\n3rd')
    else:
        print('\n' + number_list + 'th')
