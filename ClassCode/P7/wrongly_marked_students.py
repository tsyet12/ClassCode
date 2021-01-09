import numpy as np

ori_marks= np.array([[90,50,40],
                     [60,30,50],
                     [60,65,65]])


wrong=np.array([[1,0,3],
                [2,4,1],
                [0,2,2]])

final=ori_marks+2*wrong
print(final)


