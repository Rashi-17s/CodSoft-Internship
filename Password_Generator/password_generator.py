
import random
import string

print("===================================")
print("       PASSWORD GENERATOR")
print("===================================")

length = int(input("Enter password length: "))
characters = string.ascii_letters + string.digits

password = ""

for i in range(length):
    password = password + random.choice(characters)

print("\nYour generated password is:", password)