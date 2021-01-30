import numpy as np
import math

path=r'C:\Users\User\Desktop\Class\ClassCode\P11\\'
data=np.genfromtxt(path+'machine.csv',delimiter=',', skip_header=1)

min=np.min(data,axis=0)
max=np.max(data,axis=0)
x=(data-min)/(max-min)

m=x.shape[0]
n=x.shape[1]

H=-1/(math.log(m))*np.sum(x/np.sum(x,axis=0)*np.log(x/np.sum(x,axis=0)+np.finfo(np.float32).eps),axis=0)
w=(1-H)/(n-np.sum(H,axis=0))


z=x*w
z_plus=np.asarray([1,1,1,1,0])
z_neg=np.asarray([0,0,0,0,1])
S_plus=np.sqrt(np.sum((z-z_plus)**2,axis=1))

S_neg=np.sqrt(np.sum((z-z_neg)**2,axis=1))

C=S_neg/(S_plus+S_neg)
R=np.argsort(C)+1
print(C)
print(R)
best=np.where(R==1)
print("Best Technology (Shannon):  Machine #", best[0]+1)

w=np.asarray([0.291,0.079,0.206, 0.188, 0.098])
z=x*w
z_plus=np.asarray([1,1,1,1,0])
z_neg=np.asarray([0,0,0,0,1])
S_plus=np.sqrt(np.sum((z-z_plus)**2,axis=1))

S_neg=np.sqrt(np.sum((z-z_neg)**2,axis=1))

C=S_neg/(S_plus+S_neg)
R=np.argsort(C)+1
print(C)
print(R)
best=np.where(R==1)
print("Best Technology (Given Weights):  Machine #", best[0]+1)
