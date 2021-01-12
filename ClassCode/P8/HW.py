import numpy as np
x=np.asarray([148,148,148,403,403,403,25,25,25,36,36,36])
x=x.reshape(4,3).T
x=np.split(x,3)
x=x[0].reshape(2,2)
y=np.asarray([[2,7,20],[1,4,9]])
x=np.concatenate((y,x),axis=1)
x[0]=np.log(x[0])+1
x[1]=np.sqrt(x[1])
x=np.split(x,2)[0][0]
print(x)
