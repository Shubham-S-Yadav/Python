'''
Please write a program which accepts basic mathematic expression from console and print the evaluation result.
Example:
If the following string is given as input to the program:
35+3

Then, the output of the program should be:
38

'''

expression = (input("Enter expression with spaces in between: "))

num1, plus, num2, equal = expression.split()

num1, num2 = int(num1), int(num2)

if plus == '+':
  print(expression+str(num1+num2))
elif plus == '-':
  print(expression+str(num1-num2))
elif plus == '/':
  print(expression+str(num1/num2))
elif plus == '**':
  print(expression+str(num1**num2))
else:
  print(expression+str(num1*num2))
