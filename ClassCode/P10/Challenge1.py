import pandas as pd

data = {'A':  [1,2,3],
        'B': [4,5,6],
        'C': [7,8,9]}
        

df = pd.DataFrame(data, columns = ['A','B', 'C'], index=['First', 'Second', 'Third'])

df=df.where(df%2==0,df-df)
df=df.query("(A+B+C)%4!=0")
df["Best"]=pd.DataFrame(["A","A","C"],index=['First','Second', 'Third'])
df1=df.lookup(df.index,df['Best'])
print(df)
print(df1)

