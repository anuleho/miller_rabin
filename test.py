import random

def Test(n):
  a = random.randint(1,n)
  if n%2 != 0:
    m = (n-1)//2
    k = 1
    while m%2==0:
      m = m//2
      k = k+1
  else:
    m = n-1
    k = 0

  b = (a**m)%n

  if b%n == 1:
    return(str(n)+" is prime")

  for i in range(0,k):
    if b%n == n-1:
      return(str(n)+" is prime")
    else:
      b = (b**2)%n
  return(str(n)+" is composite")

print(Test(29))
print(Test(565))
print(Test(74))
import random



