import pandas as pd

data=[[1,2,3],[4,5,6],[7,8,9]]

df = pd.DataFrame (data, columns = ['A','B', 'C'], index=['First', 'Second', 'Third'])

print(df)

#Directly index column name
print(df[['A']])

#Use iloc for integer index
print(df.iloc[0,1])

#Use loc for index name
print(df.loc['Second'])


