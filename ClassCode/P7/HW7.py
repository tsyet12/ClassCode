import numpy as np

path=r'C:\Users\User\Desktop\Class\ClassCode\P7\\'

marks= np.genfromtxt(path+'who_fail.csv',delimiter=',',skip_header=True)

norm= (marks-np.min(marks))/(np.max(marks)-np.min(marks))

weights=np.array([[3]*5,[1]*5,[2]*5])
final=np.sum(norm*weights,axis=0)/(3+1+2)
print(final)
