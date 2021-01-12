import numpy as np

a=np.array([1,2,3])
b=np.array([4,5,6])

c=np.array([[1,2,3],[4,5,6]])
d=np.array([[5,6,7],[8,9,10]])

print("concatenate axis=0:\n",np.concatenate((a,b),axis=0))
#print("concatenate axis=0:\n",np.concatenate((c,d),axis=0))
#print("concatenate axis=1:\n",np.concatenate((c,d),axis=1))



print("stack axis=1:\n",np.stack((a,b),axis=1))
print("stack axis=0:\n",np.stack((a,b),axis=0))
print("horizontal stack:\n",np.hstack((a,b)))

print("vertical stack:\n",np.vstack((a,b)))
print("depth stack:\n",np.dstack((a,b)))
