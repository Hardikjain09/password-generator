import string
import random
import pyperclip 

alphabets = list(string.ascii_lowercase + string.ascii_uppercase)
digits = list(string.digits)
symbols = list("!@#$%^&*()-_=+[]{}|;:',.<>?/`~")

n_alpha = int(input("Enter the number of alphabets: "))
n_digit = int(input("Enter the number of digits: "))
n_symbol = int(input("Enter the number of symbols: "))


password_list = []
for char in range(n_alpha):
    password_list.append(random.choice(alphabets))
for char in range(n_digit):
    password_list.append(random.choice(digits))
for char in range(n_symbol):
    password_list.append(random.choice(symbols))
    
random.shuffle(password_list)
password = "".join(password_list)
print(f"Your password is: {password}")
pyperclip.copy(password)
print("Password copied to clipboard.")