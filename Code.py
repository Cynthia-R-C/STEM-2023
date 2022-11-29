import math

'''Other Functions'''
def fractpt(x):
  return x-math.floor(x)
def isprime(x):
  for i in range(2,x):
    notdivis=math.ceil(fractpt(x/i))
    if notdivis==0:
      return False
  return True

#Prime number tests
#for i in [3,12,121,23]:
#  print(isprime(i))

def isdivisible(x,y):
  '''Tests if x is divisible by y'''
  if math.ceil(fractpt(x/y))==0:
    return True
  else:
    return False

#isdivisble() tests
#print(isdivisible(4,2))
#print(isdivisible(5,3))
#print(isdivisible(49,7))

n=int(input("Enter the vertical side length of the grid. "))
m=int(input("Enter the horizontal side length of the grid. "))

'''Regular Rectangles'''
regularrects=int((m*n*(m+1)*(n+1))/4)
print("There are",regularrects,"regular rectangles.")

'''Diagonal Rectangles'''
'''V = H, k = 1'''
#This is the one for squares: the sum of d(n - d)^2 where d goes from 1 to n - 1
diagonalsq=0
for d in range(1,min(m,n)):
  diagonalsq+=d*(m-d)*(n-d)
print("There are",diagonalsq,"diagonal squares.")

'''V = H, k != 1'''  
#This is the one for non-square diagonal rectangles that fit in a square
sqDiagRects=0
def numoftypes(V):
  totsum=0
  prevsum=0
  for i in range(1,V+1):
    totsum+=math.floor(V/i)
  totsum-=(3*(math.floor(V/2))+math.ceil(fractpt(V/2)))
  for i in range(1,V):
    prevsum+=math.floor((V-1)/i)
  prevsum-=(3*(math.floor((V-1)/2))+math.ceil(fractpt((V-1)/2)))
  return (totsum-prevsum)

for V in range(2,min(m,n)+1):
  sqDiagRects+=(m-V+1)*(n-V+1)*2*numoftypes(V)
print("There are",sqDiagRects,"diagonal rectangles that fit into a square.")

#numoftypes(V) test
#for i in range(2,13):
#  print(numoftypes(i))
 
'''V != H, H < V'''
rectDiagRects1=0
possiblevalues1=[]
def numoftypes2(V):
  '''Calculates the number of possible types of diagonal rectangles
such that H < V. Values should follow the pattern 0,0,0,1,0,2,1,2,2,4,1 (as long as m > a certain H) and should also add all possible values of H into a list'''
  numoftypes=0
  for a in range(1,math.floor((V-2)/3)+1):
    for k in range(2,V-2):
      if a*(1+k)<=V-2:
        if isdivisible(V-a,k):
          b=(V-a)/k
          H=int(b+a*k)
          if H<=m:
            numoftypes+=1
            possiblevalues1.append(H)
  return numoftypes

for V in range(1,n+1):
  possiblevalues1=[]
  numoftypes2(V)
  for H in possiblevalues1:
    rectDiagRects1+=(n-V+1)*(m-H+1)*2
print("There are",rectDiagRects1,"diagonal rectangles that don't fit in a square and satisfy H < V.")

#nummoftypes2(V) tests
#for V in [2,3,4,5,6,7,8,9,10,11,12]:
#  print(numoftypes2(V))

'''V != H, H > V'''
rectDiagRects2=0
possiblevalues2=[]
def numoftypes3(V):
  '''Calculates the number of possible types of diagonal rectangles such that H > V. Values should follow pattern 0,0,1,2,3,5,6,8,10,12,13 (as long as m > a certain H) and should also add all possible values of H into a list'''
  numoftypes=0
  for b in range(1,math.floor((V-1)/3)+1):
    for k in range(2,V-1):
      if b*(1+k)<=V-1:
        a=V-b*k
        H=int(b+a*k)
        if H<=m:
          numoftypes+=1
          possiblevalues2.append(H)
  return numoftypes

for V in range(1,n+1):
  possiblevalues2=[]
  numoftypes3(V)
  for H in possiblevalues2:
    rectDiagRects2+=(n-V+1)*(m-H+1)*2
print("There are",rectDiagRects2,"diagonal rectangles that don't fit in a square and satisfy H > V.")

#nummoftypes3(V) tests
#for V in [2,3,4,5,6,7,8,9,10,11,12]:
#  print(numoftypes3(V))

print("There are",regularrects+diagonalsq+sqDiagRects+rectDiagRects1+rectDiagRects2,"rectangles total.")
