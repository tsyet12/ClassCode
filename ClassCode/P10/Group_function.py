import pandas as pd

data = {'A':  ["Good","Bad","Good"],
        'B': ["Yes","Yes","No"],
        'C': [7,8,9]}
        

df = pd.DataFrame(data, columns = ['A','B', 'C'], index=['First', 'Second', 'Third'])


df=df.groupby("A")

print(df)

