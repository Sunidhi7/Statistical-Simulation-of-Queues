import random
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
N = 10000

# Generating exponential random variable
lambda_e = 2
U = np.random.random(N)
X = -np.log(U) / lambda_e

print(X)


  































#X = np.zeros(N)
#for i in range(N):
#    X[i] = np.log(M[i])/lambd
