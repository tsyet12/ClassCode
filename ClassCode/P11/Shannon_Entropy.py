import numpy as np
import math

path=r'C:\Users\User\Desktop\Class\ClassCode\P11\\'
x=np.genfromtxt(path+'data_norm.csv',delimiter=',')
m=x.shape[0]
n=x.shape[1]

H=-1/(math.log(m))*np.sum(x/np.sum(x,axis=0)*np.log(x/np.sum(x,axis=0)+np.finfo(np.float32).eps),axis=0)
w=(1-H)/(n-np.sum(H,axis=0))


print(w)

z=x*w
z_plus=np.asarray([0,0,1,1,1])
z_neg=np.asarray([1,1,0,0,0])
S_plus=np.sqrt(np.sum((z-z_plus)**2,axis=1))

S_neg=np.sqrt(np.sum((z-z_neg)**2,axis=1))

C=S_neg/(S_plus+S_neg)
R=np.argsort(C)+1
print(C)
print(R)
