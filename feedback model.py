from math import *
import numpy as np
import scipy.integrate as sc
import matplotlib.pyplot as plt

#Initialize

def absorb(x):
    return 0.1016125 - (1.29*x)/(100000)
    
#arsinh(2/5) = 0.39
#k = 20pi/vph = 0.1904
#4pi/vph = 0.0381

def integrand(f,x,y):
    I = 4 * cos(0.0381*f* sqrt(25+x**2+y**2))*0.0381*(1/sqrt(25+x**2+y**2))
    return I

def interfere(f0):
    
    A = sc.nquad(integrand, [[0, f0], [0, 2], [0, 2]])
    return(A[0])
#x keeps frequencies

x = np.linspace(100, 200, 200)

#y keeps amplitudes

y = np.exp(-(((x/100)-1.5)*5)**2)
#y1 initialized as arbitrary array with 200 values

y1 = absorb(x) * y

y1 = np.vectorize(interfere)(x) * y1

y1 = np.abs(y1)

plt.scatter(x,y)
plt.scatter(x,y1)
plt.show()