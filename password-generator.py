# Libraries needed 
import random
import string

# Generate password function
def generate_password():
    # User enters the length of password 
    length = int(input("Enter password length: "))

    # If the length of password less than 4, warning message will be printed
    if length < 4:
        print(" Warning: Password length is very short and not secure. ")

    # User chooses using symbols or not
    use_symbols = input("Include symbols? (y/n): ").lower()


    characters = string.ascii_letters + string.digits

    # Symbols will be used in password if user chose yes
    if use_symbols == 'y':
        characters += string.punctuation

    # Password will be generated
    password = ''.join(random.choice(characters) for _ in range(length))

    # Print generated password
    print("Generated password:", password)

while True:
    generate_password()
    again = input("Generate another password? (y/n): ").lower()
    if again != 'y':
        print("Goodbye!")
        break





