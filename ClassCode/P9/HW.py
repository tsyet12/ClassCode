import pandas as pd
import numpy as np
path=r"C:\Users\User\Desktop\Class\ClassCode\P9\\"
df = pd.read_excel(path+"HW.xlsx")

df=df.drop_duplicates()
df=df.sort_values("Cost")
x=df.values

x=x[:-1,:]

value=x[:,1:]
tech=x[:,0]

norm_value=(value-np.min(value,axis=0))/(np.max(value,axis=0)-np.min(value,axis=0))

weights=[1.3,1,-0.9]
w_value=norm_value*weights
w_sum=np.sum(w_value,axis=1)/np.sum(weights)

w=np.vstack((tech,w_sum)).T

df=pd.DataFrame(w)
df=df.sort_values(1)
print(df.values[-1])

