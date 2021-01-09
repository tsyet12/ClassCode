import numpy as np

path=r'C:\Users\User\Desktop\Class\ClassCode\P7\\'

x= np.genfromtxt(path+'read.csv',delimiter=',',skip_header=True)

print(x)

