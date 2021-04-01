print("Enter a character:")

char = input()

if(char.islower()):
    print(char, 'is a lower case letter.')
elif(char.isdigit()):
    print(char, 'is a digit.')
elif(char.isupper()):
    print(char, 'is an upper case letter.')
else:
    print(char, 'is a non-alphanumeric character.')
