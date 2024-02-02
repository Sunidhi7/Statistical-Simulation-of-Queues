import math
import random
import numpy as np
import matplotlib.pyplot as plt

N = 100000

# Generating Poisson random variable
lambda_p = 8
X = []
for i in range(N):
  n = 0
  p = 1
  while p > np.exp(-lambda_p):
    p = p*np.random.random()
    n = n + 1
  X.append(n-1) 

def prob(x):
  count = 0
  for i in range(N):
      if X[i] == x:
          count = count + 1

  return(count/100000.0)

#Factorial of a number
def factorial(q):
   if q == 0:
       return 1
   else:
       return q*factorial(q-1)


x = np.arange(0, np.amax(X)+1 , 1)
y = [prob(i) for i in x]
y1 = [(math.exp(-lambda_p)*(lambda_p)**i)/ factorial(i)  for i in x]
plt.plot(x, y, 'r', marker='o', label ='Simulated pmf')
plt.plot(x, y1, 'b', marker='o', label = 'Theoretical pmf')
plt.xlabel('n')
plt.ylabel('pmf')
plt.legend(loc="upper right")
plt.show()


