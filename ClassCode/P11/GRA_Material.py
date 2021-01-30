import numpy as np
import math

path=r'C:\Users\User\Desktop\Class\ClassCode\P11\\'
data=np.genfromtxt(path+'Material.csv',delimiter=',', skip_header=1)

min=np.min(data,axis=0)
max=np.max(data,axis=0)
x=(data-min)/(max-min)


ideal=np.asarray([1,1])

delta=np.abs(x-ideal)
delta_min=np.min(delta)
delta_max=np.max(delta)
c=0.5
GRC=(delta_min+c*delta_max)/(delta+c*delta_max)
n=delta.shape[1]
GRG=np.sum(GRC,axis=1)/n
R=np.argsort(GRG)+1
best=np.where(R==1)
print(R)
print("Best Material (GRA):  Material #", best[0]+1)


''''

m=x.shape[0]
n=x.shape[1]

H=-1/(math.log(m))*np.sum(x/np.sum(x,axis=0)*np.log(x/np.sum(x,axis=0)+np.finfo(np.float32).eps),axis=0)
w=(1-H)/(n-np.sum(H,axis=0))


z=x*w
z_plus=np.asarray([1,1])
z_neg=np.asarray([0,0])
S_plus=np.sqrt(np.sum((z-z_plus)**2,axis=1))

S_neg=np.sqrt(np.sum((z-z_neg)**2,axis=1))

C=S_neg/(S_plus+S_neg)
R=np.argsort(C)+1
#print(C)
print(R)
best=np.where(R==1)
print("Best Technology (Shannon):  Material #", best[0]+1)

