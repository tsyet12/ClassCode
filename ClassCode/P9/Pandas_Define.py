import pandas as pd

data = {'A':  [1,1,1],
        'B': [2,2,2],
        'C': [3,3,3]}
        
     
data=[[1,1,1],[2,2,2],[3,3,3]]

df = pd.DataFrame(data, columns = ['A','B', 'C'], index=['First', 'Second', 'Third'])

print(df)