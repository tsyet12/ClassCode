import pandas as pd

data = {'A':  [1,2,3],
        'B': [4,5,6],
        'C': [7,8,9]}
        

df = pd.DataFrame(data, columns = ['A','B', 'C'], index=['First', 'Second', 'Third'])
print(df)
#print(df.query("(A+B)%3==0"))
#print(df.query("(A+B)%3!=0"))
#print(df.query("A*B*C<=80"))





