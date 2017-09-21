'''
An n-bit Gray code is a sequence of n-bit strings constructed according to certain rules.

For example,
n = 1: C(1) = ['0','1'].
n = 2: C(2) = ['00','01','11','10'].
n = 3: C(3) = ['000','001','011','010','110','111','101','100'].

Find out the Gray code for given no. (between 1 to 10)


'''

def grayCode(iNo):
  def grayCode_recurse (g,iNo):
     print(g, iNo)
     k = len(g)
     if iNo <= 0:
       return

     else:
       for i in range (k-1, -1, -1):
          char = '1' + g[i]
          g.append(char)
       for i in range (k-1, -1, -1):
          g[i] = '0' + g[i]

       grayCode_recurse (g, iNo - 1)

  g = ['0','1']
  grayCode_recurse(g, iNo - 1)
  return g

def main():
  iNo = int(input("Enter number between 1 to 10: "))
  g = grayCode (iNo)

  if iNo >= 1:
    for i in range (len(g)):
       print(g[i])

main()