import numpy as np
path=r'C:\Users\User\Desktop\Class\ClassCode\P11\\'
data=np.genfromtxt(path+'technology.csv',delimiter=',',skip_header=1)
print(data)

min=np.min(data,axis=0)
max=np.max(data,axis=0)
norm1=(data-min)/(max-min)

np.savetxt(path+'data_norm.csv',norm1,delimiter=',')

