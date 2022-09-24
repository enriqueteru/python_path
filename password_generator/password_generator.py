import random

print("Let´s create some password!:")
print("============================\n\n")

number = input("Amount of password/s to generate: ")
number = int(number)

length = input("Length of the password/s: ")
length = int(length)

hash = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYZ()$%&.*$@"

print("\nYour password/s: ")


def generate(hash, number, length):
    for pwd in range(number):
        password = ""
        for c in range(length):
            password += random.choice(hash)
        print(password)
        
        
generate(hash, number, length)        
