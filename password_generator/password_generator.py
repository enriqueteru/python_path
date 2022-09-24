import random

print("Let´s create some password!:")
print("============================\n")

number = int(input("Amount of password/s to generate: "))
length = int(input("Length of the password/s: "))
hash = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYZ()$%&.*$@"

print("\nYour password/s:")
print("============================\n")

def generate(hash, number, length):
    for pwd in range(number):
        password = ""
        for c in range(length):
            password += random.choice(hash)
        print(password + "\n")


generate(hash, number, length)
