'''
Write a function to divide a number 100 by user input no. and use try/except to catch the exceptions.

'''

def div(iNo):
  try:
      iResult = 100/iNo
      if iResult < 0:
       raise NegativeNumberException#("Please enter positive integer.")
      print("100 / "+str(iNo)+" = {:.2f}".format(iResult))
  except ValueError:
      print("Oops!  That was no valid number.  Try again...")
  except ZeroDivisionError:
      print("0 can't be divided by any number. Please try another number.")
  except NegativeNumberException:
      print("Please enter positive integer.") 
  except:
      print("Unknown Error occured.")

iNo = int(input("Enter number to be divided by 100: "))
div(iNo)
      