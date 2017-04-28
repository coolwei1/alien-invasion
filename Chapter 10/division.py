print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	try:
		int(first_number)
	except ValueError:
		print("Please enter number!")
	else:
		second_number =input("Second number: ")
		try:
			answer = int(first_number)/int	(second_number)
		except ZeroDivisionError:
			print("You can't divide by zero!")
		except ValueError:
			print("Please enter number!")
		else:
			print(answer)