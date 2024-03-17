import numpy as np 
import random as ran
from matplotlib import pyplot as plt 

N = 500 
n = 1
e0 = 1
edelta = e0 
nsteps = 10000
array = np.zeros(N)
for i in range(N):
    array[i]= e0 + n*edelta


t=0
while t<nsteps:
    t=t+1
    x1 = ran.randrange(N)
    if array[x1]>e0:
        x2 = ran.randrange(N)
        array[x1] = array[x1]-edelta
        array[x2] = array[x2]+edelta 

newarray = array        
print (newarray)

sume=0
for i in range(N):
    sume=sume+newarray[i]
    
print(sume)

index = np.arange(500)
x = index
y = newarray[x]
plt.xlabel("array index")
plt.ylabel("particle energy")
plt.title("Plot of energy particle in array as a function of its index number")
plt.bar(x,y)
plt.show()

intarray = newarray.astype(int) 
n_bins = np.max(intarray)
plt.hist(intarray, bins=n_bins)
plt.xlabel("particle energy values")
plt.ylabel("particle count with that energy value")
plt.title("Plot to find expected Boltzmann distribution")
plt.show()
