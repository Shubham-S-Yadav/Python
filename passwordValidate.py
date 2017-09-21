'''
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12

Your program should accept a password and will check them according to the above criteria. 
Passwords that match the criteria should print:
"Password matches with the password policy."
Otherwise.    
"Password not matches with the the password policy."

'''

import symbol

password = (input("Enter password: "))

small = 0
capital = 0
digit = 0
symbol = 0

len = len(password)

if len < 6:
  print("Password too short.")
  pass

if len > 12:
  print("Password is too big.")
  pass

for char in password:
  if char.isalpha():
    if char > 'a' and char < 'z':
      small = small + 1
    else:
      capital = capital + 1
  elif char.isdigit():
      digit = digit + 1
  #elif symbol.issymbol(char):
      #symbol = symbol + 1
  else:
      symbol = symbol + 1
if small > 0 and capital > 0 and digit > 0 and symbol > 0:
   print("Valid Password.")
else:
   print("Invalid Password.")