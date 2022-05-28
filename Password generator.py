#A strong password generator

import random

#list of items
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#
print("Welcome to the Yami's Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = [] #Empty list to add random characters

for char in range(1, nr_letters+1):  #random pick from letters list
    rand_character = random.choice(letters)
    password += rand_character

for sym in range(1,nr_symbols+1): #random pick from symbols list
    rand_sym = random.choice(symbols)
    password += rand_sym

for numb in range(1,nr_numbers+1):  #random pick from numbers list
    rand_num = random.choice(numbers)
    password += rand_num

# print(password)
random.shuffle(password) #generated list of items "password" shuffled


finalPass = "" #New string of shuffled items of the "password" list
for char in password:
    finalPass += char
print("Your generated password is : \n" + finalPass)




