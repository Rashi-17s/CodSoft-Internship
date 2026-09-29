
import secrets
import string

print("===================================")
print("       PASSWORD GENERATOR")
print("===================================")

while True:
    try:
        length = int(input("\nEnter password length: "))

        if length < 6:
            print("Password length must be at least 4.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")

print("\nChoose password options:")
uppercase = input("Include uppercase letters? (yes/no): ").lower()
numbers = input("Include numbers? (yes/no): ").lower()
symbols = input("Include special characters? (yes/no): ").lower()

characters = string.ascii_lowercase
required = []

if uppercase == "yes":
    characters += string.ascii_uppercase
    required.append(secrets.choice(string.ascii_uppercase))

if numbers == "yes":
    characters += string.digits
    required.append(secrets.choice(string.digits))

if symbols == "yes":
    characters += string.punctuation
    required.append(secrets.choice(string.punctuation))

if length < len(required):
    print("Password length is too short.")

else:
    while True:
        password = required.copy()

        while len(password) < length:
            password.append(secrets.choice(characters))

        secrets.SystemRandom().shuffle(password)

        print("\nGenerated Password:", "".join(password))

        choice = input("\nGenerate another password? (yes/no): ").lower()

        if choice != "yes":
            print("Thank you for using Password Generator!")
            break