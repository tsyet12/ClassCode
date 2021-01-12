import numpy as np

x=np.array([1,2,3])

print('repeat\n',np.repeat(x,5))
print('tile\n',np.tile(x,5))

x1=np.array([[1,2,3],[4,5,6]])
print('repeat axis=0\n', np.repeat(x1,5,axis=0))
print('repeat axis=1\n', np.repeat(x1,5,axis=1))
print('tile\n',np.tile(x1,5))
