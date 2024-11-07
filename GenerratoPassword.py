
# PROJECT DAY_5 PASSWORD_GENAERATOR
import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y' , 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols =['!', '#', '$', '%', '＆', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int (input(f"How many numbers would you like?\n"))
nr_symbols = int (input(f"How many synmbols would you like?\n"))
# length of lists
num_letters = len(letters)
num_numbers = len(numbers)
num_symbols = len(symbols)
#  random choice letters
nr_letters_choice = 1
my_letters=[]
for letter in letters:
  if nr_letters_choice<=nr_letters:
    nr_letters_choice+=1
    choice_letter = random.randint(0, num_letters - 1)
    my_letters.append(letters[choice_letter])
# print(my_letters)
#  random choice numbers
nr_numbers_choice = 1
my_numbers=[]
for number in numbers:
  if nr_numbers_choice<=nr_numbers:
    nr_numbers_choice+=1
    choice_number = random.randint(0, num_numbers - 1)
    my_numbers.append(numbers[choice_number])
# print(my_numbers)
#  random choice symbols
nr_symbols_choice = 1
my_symbols = []
for symbol in symbols:
  if nr_symbols_choice<=nr_symbols:
    nr_symbols_choice+=1
    choice_symbol = random.randint(0, num_symbols - 1)
    my_symbols.append(symbols[choice_symbol])
# print(my_symbols)
# extend list
my_letters.extend(my_numbers)
my_letters.extend(my_symbols)
passwords = my_letters
# result : my password
nr_passwords = len(passwords)
nr_password_choice = 1
my_password = []
for password in passwords:
  if nr_password_choice<=len(passwords):
    nr_symbols_choice+=1
    choice_password = random.randint(0, len(passwords) - 1)
  my_password.append(passwords[choice_password]) 
password = ''.join(str(item) for item in my_password)
print(f"Your password is: \n {password}")
