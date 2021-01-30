import pandas as pd
data = {'A':  [1,2,3],
        'B': [4,5,6],
        'C': [7,8,9]}
        
df = pd.DataFrame(data, columns = ['A','B', 'C'], index=['First', 'Second', 'Third'])
print(df)

#Drop
df1=df.drop(['First','Second'],axis=0)
print(df1)

df2=df.drop(['A','B'],axis=1)
print(df2)

#Concatenate
df3=pd.concat([df1,df2],axis=1)
print(df3)


#Reindex
df4=df.reindex(["C","B","A"],axis=1)
print(df4)


df5=df.reindex(["Second","Third","First"],axis=0)
print(df5)

