#message = input("Tell me something, and I will reply it back to you\n")
#print("\nSystem: " + (message))

prompt = "\nTell me something, and I will reply it back to you."
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)