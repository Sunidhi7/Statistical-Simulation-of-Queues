#Uniform Random Number Generator

import random
import matplotlib.pyplot as plt
import numpy as np 

#Generating random numbers between [0,1).
random.seed(123) #Setting the seed
M = np.random.random(100000) #Generating a 1 by 10000 array of random numbers between 0 and 1.

#CDF
def prob(x):
  count = 0
  for i in range(100000):
      if M[i-1] > x:
          count = count + 1
  return(count/100000.0)

#Plot
x = np.arange(0.0, 1.0, 0.0001)
y = [1-prob(i) for i in x]
x2 = np.arange(0.0, 1.0, 0.0001)
y2 = [i for i in x] #For uniform random variable, P(X <= x) = x for x in [0,1]
plt.plot(x, y, 'b', label = 'Simulated CDF')
plt.plot(x2, y2, 'r', label = 'Theoretical CDF')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('x') 
plt.ylabel('P(U<=x)') 
plt.legend()
plt.show()



#x = np.arange(0.4, 0.61, 0.0001)
#y = [prob(i) for i in x]
#plt.plot(x, y)
#plt.xlim([0.4, 0.6])
#plt.xlabel('x') 
#plt.ylabel('Pr(U>x)') 
#plt.show()



