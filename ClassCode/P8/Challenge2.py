import numpy as np
x=np.asarray([1,2,3,5,6])
x=np.tile(x,3).reshape(3,5)
x[1]=np.exp(x[1])
x[2]=np.square(x[2])
x=x[1:]
x=x.T
x=x[np.sum(x,axis=1)>50]
x=x.T
x=np.repeat(x.reshape(4),3)
print(x)