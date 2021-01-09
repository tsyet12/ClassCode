import numpy as np

path=r'C:\Users\User\Desktop\Class\ClassCode\P7\\'

marks= np.genfromtxt(path+'bias_teacher.csv',delimiter=',',skip_header=True)

gift=np.array([1,1,0]*3).reshape(3,3)
homework=np.array([1,0,1]*3).reshape(3,3)

final_marks=marks+gift*np.random.rand(3,3)*10+homework*-5

print(final_marks)

np.savetxt(path+'final_marks.csv', final_marks, delimiter=',')


