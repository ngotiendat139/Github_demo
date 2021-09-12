import numpy as np
import random
import math

#Exercise_a
x = list(np.random.choice([0, 1, 2, 3, 4, 5], 3650, p=[ 0.1, 0.2, 0.3, 0.2, 0.15, 0.05]))
X = set(x)
print('The result of Exercise a is: ', X)

#Exercise_b
def PD(x, X):
   return [x.count(i)*1.0/len(x) for i in X]
P = PD(x, X)
print('The result of Exercise b is: ', P)

#Exercise_c
def Expectation(X, P):
    E_X = 0
    pos = 0
    for i in X:
       E_X += i * P[pos]
       pos += 1 
    return E_X
E_X = Expectation(X, P)      

def Variance(X, P):
    E_X = Expectation(X, P)  
    Var_X = 0
    pos = 0
    for i in X:
        Var_X += (i - E_X) * (i - E_X) * P[pos]
        pos += 1
    return Var_X
Var_X = Variance(X, P)
SD_X = math.sqrt(Var_X)

print('The result of E_X is: ', E_X)
print('The result of Var_X is: ', Var_X)
print('The result of standard deviation is: ', SD_X)

#Exercise_d
def Probability(X):
    a = 0
    for i in X:
        if(i>=3):
            a +=P[i]
    return a
print('The result of Exercise d is: ',Probability(X));