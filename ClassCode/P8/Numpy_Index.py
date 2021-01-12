import numpy as np

x=np.array([[1,2,3],[4,5,6],[7,8,9]])

Q1=x[2][1]
#Q1=x[2,1]
print(Q1)

Q2=x[:,1:3]
print(Q2)

x3=np.array([1,7,2,5,3,5,6)
Q3=x3[x3<4]
print(Q3)

#Q4=x[np.sum(x,axis=1)<7][0]
Q4=x[x.sum(axis=1)<7][0]
print(Q4)
