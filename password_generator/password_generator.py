import random
print('Let´s create some password!:')
print('============================\n\n')

hash = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYZ()$%&.*$@'

number = input('Amount of password/s to generate: ')
number = int(number)

length = input('Length of the password/s: ')
length = int(length)

print('\nYour password/s: ')


for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(hash)
    print(password)