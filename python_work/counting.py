current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#7.4 - 7.5
while True:
    prompt = input("Enter a topping you want to add into your pizze.\n(Enter 'quit' to stop) ")

    if prompt == 'quit':
        break
    print("I'll add " + prompt + " topping into your pizze")


while True:
   prompt = input("How old are you? \nEnter 'quit' to stop")
   
   if prompt == 'quit':
       break
   
   prompt = int(prompt)
   
   if prompt < 3:
       print("Your ticket is free")
   elif prompt < 13:
       print("Your ticket costs $10")
   else:
       print("Your ticket costs $15")

