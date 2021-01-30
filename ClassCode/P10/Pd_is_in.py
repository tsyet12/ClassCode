import pandas as pd

data = {'A':  [1,2,3],
        'B': [4,5,6],
        'C': [7,8,9]}
        
df = pd.DataFrame(data, columns = ['A','B', 'C'], index=['First', 'Second', 'Third'])

print(df)

print(df.isin([1,5,9]))



print(df.isin({'A':[2,3,5]}))

data2 = {'A':  [1,2],
        'B': [4,5]}
        
df2 = pd.DataFrame(data2, columns = ['A','B'], index=['First', 'Second'])
print(df2)
print(df.isin(df2))

