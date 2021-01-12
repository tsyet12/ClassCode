import numpy as np
'''
x=np.array([[1,2],[3,4],[5,6]])
print(x)
print(x.reshape(2,3))

print(x.T) #this is transpose
'''

x1=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print('x1: \n',x1)
print('x1 reshaped:\n',x1.reshape(1,4,2))
