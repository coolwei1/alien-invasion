import json


try:
	filename = 'Chapter 10/fav_no.txt'
	with open(filename) as f_object:
		fav_no = json.load(f_object)
except FileNotFoundError:
	fav_no = input("Enter your favorite number: ")
	with open('Chapter 10/fav_no.txt', 'a') as f_object:
		json.dump(fav_no, f_object)
else:
	print("I know your favorite number! It's " + fav_no + ".")
