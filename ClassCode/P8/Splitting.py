import numpy as np

x=np.array([[[1,2],[3,4]],
            [[5,6],[7,8]]])

print('array_split axis=0:\n', np.array_split(x,2,axis=0))
print('array_split axis=1:\n', np.array_split(x,2,axis=1))


x1=np.array([1,2,3,4,5,6,7])
print('split axis=0:\n', np.split(x1,[3,6],axis=0))


print('horizontal split=\n', np.hsplit(x,2))
print('vertical split=\n', np.vsplit(x,2))
print('depth split=\n', np.dsplit(x,2))
