num = int(input())
from math import sqrt
c=0
for i in range(2,int(sqrt(num)+1)):
    if num%i == 0:
        c+= 1
if c == 0:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
    
