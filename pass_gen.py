#importing random and string module
import random
import string

s_char = '!@#$%^&*.-_'
chars = (string.ascii_letters + string.digits + s_char)

length = input("Insert password length: ")
length = int(length)

password = ''
for c in range(length):
    password += random.choice(chars)
print("Your password is: {} . Write it down!".format(password))
# Will replace {} with password

