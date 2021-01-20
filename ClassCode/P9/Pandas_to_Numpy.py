import pandas as pd

data=[[1,2,3],[4,5,6],[7,8,9]]

df = pd.DataFrame (data, columns = ['A','B', 'C'], index=['First', 'Second', 'Third'])

print(df)

#Pandas to Numpy
x=df.values
print(x)


#Numpy back to Pandas
df2=pd.DataFrame(x, columns=df.columns, index=df.index)
print(df2)

