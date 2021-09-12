import numpy as np
import math

#Exercise_a
x= list(np.random.choice([0,1,2],10000,p=[0.25,0.5,0.25]))

#Exercise_b
X=set(x)

#Exercise_c
def ProbabilityDistribution(x,X):
    return [x.count(i)*1.0/ len(x) for i in X]
P=ProbabilityDistribution(x,X)

print('The result of Exercise c is: ',P)

#Exercise d
def  Expectation(X,P):
    E=0
    index=0
    for i in X:
        E +=i*P[index]
        index +=1
    return E

def Variance(X,P):
    E=Expectation(X,P)
    Var=0
    index=0
    for i in X:
        Var+=(i-E)*(i-E)*P[index]
        index+=1
    return Var
    
print('E(X):',Expectation(X,P))
print('Var(X):',Variance(X,P))
print('The result of standard deviation is: ',math.sqrt(Variance(X,P)))

#Exercise_e
def Pro(X):
    Xs=0
    for i in X:
        if(i>=1):
            Xs +=P[i]
    return Xs

print('The result of Exercise e is: ',Pro(X));