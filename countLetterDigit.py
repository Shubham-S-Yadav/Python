'''
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:
hello world! 123

Then, the output should be:
LETTERS 10
DIGITS 3

'''

sentence = input("Enter a sentence: ")

alpha = 0
digit = 0

for char in sentence:
  if char.isalpha():
    alpha = alpha + 1
  elif char.isdigit():
    digit = digit + 1
  else:
    pass

print("Letters: ", alpha)
print("Digits: ", digit)