'''
Write a program that computes the net amount of a bank account based a transaction log from file. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100

Then, the output should be:
Total Deposit = 700
Total Withdrawal = 200
Total Balance = 500
'''

B = 0
D = 0
W = 0


while True:

  transaction = input("Enter TYPE of transaction only [Deposite: D/Withdraw: W] ")

  transaction1, transaction2 = transaction.split(" ")
  print(transaction[0], transaction[2])

  amount = int(transaction2)

  if transaction1 == 'D' or transaction1 == 'd':
    D = D + amount
    B = B + amount
  elif transaction1 == 'W' or transaction1 == 'w':
    if B <= amount:
      print("Not Sufficient Balance.\nTransaction failed.");
      break
    else:
      B = B - amount
      W = W + amount
  elif transaction1 == 'E' or transaction1 == 'e':
    break
  else:
    print("Invalid Input.")

print("Total Balance: Rs.", B)
print("Total Deposited amount: Rs.", D)
print("Total Withdrawal amount: Rs.", W)