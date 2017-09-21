'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,  then tell them whether they guessed too low, too high, or exactly right.

'''

import random 

while True:
  number = int(input("Enter a number between 1 to 10: "))
  rand = random.randrange(1, 10)

  if (number == rand):
   print("You guessed it right")
   break
  elif number > rand:
   print("Guessed too high.")
  else:
   print("Guessed too low.")