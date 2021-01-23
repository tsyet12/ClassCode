import pandas as pd
import numpy as np
data = {'A':  [1,2,3,4],
        'B': [4,5,6,7],
        'C': [7,8,9,10]}
        

df = pd.DataFrame(data, columns = ['A','B', 'C'], index=['First', 'Second', 'Third', 'Forth'])

df1=df.drop("Second",axis=0)
df1=df1.where(df%2!=0, df/2)
df2=pd.DataFrame({"D":[1,2,3]},index=df1.index)
print(df2)
df1=pd.concat([df1,df2],axis=1)

df1=df1.reindex(df1.columns[::-1],axis=1)
df1=df1.reindex(df.index,axis=0)

df1=df1.fillna(0)
print(df1)
