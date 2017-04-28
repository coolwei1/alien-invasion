age = 18
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")

age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")

#exercise
alien_colors = ['green', 'yellow', 'red']
if 'green' in alien_colors:
    print("5 points earned!")
if 'yellow' not in alien_colors:
    print("0 point earned!")

alien_colors = ['green', 'yellow', 'red']
if 'green' in alien_colors:
    print("5 points earned!")
if 'yellow' in alien_colors:
    print("10 points earned!!")
if 'red' in alien_colors:
    print("10 points earned!!")

print("Good job")

# 22 2 2 2 2 2 
age = 2
if age < 2:
    print("Baby")

elif age < 4:
    print("toddler")

elif age < 13:
    print("kid")

elif age < 20:
    print("teenager")

elif age < 65:
    print("adult")

else:
    print("elder")

favorite_food = ['banana', 'apple', 'durian', 'pineapple', 'watermellon']
if 'banana' in favorite_food:
    print("I really like banana")
if 'apple' in favorite_food:
    print("I really like apple")

name, age = 'Richard', 100
print(name, age)
print(age)
