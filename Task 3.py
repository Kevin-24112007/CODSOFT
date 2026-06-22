import string
import random

print("----------PASSWORD GENERATOR----------\n")

password_length = int(input("Enter the password length: "))
print("\nChoose password complexity\n1. Easy(Letters only)\n2. Medium(Letters and Numbers only)\n3. Strong(Letters,Numbers and Symbols)\n")
ch = int(input("Enter your choice: "))
if ch == 1:
    characters = string.ascii_letters
elif ch == 2:
    characters = string.ascii_letters + string.digits
elif ch == 3:
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid choice, default complexity - Strong")
    characters = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(password_length):
    password += random.choice(characters)

print(f"\nPassword generated: {password}")