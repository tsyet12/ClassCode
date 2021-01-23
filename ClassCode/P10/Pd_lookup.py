import pandas as pd

data = {'A':  [1,2,3],
        'B': [4,5,6],
        'C': [7,8,9],
        'Best':['A','C','C']}
        

df = pd.DataFrame(data, columns = ['Best','A','B', 'C'], index=['First', 'Second', 'Third'])

df['value'] = df.lookup(df.index, df['Best'])

print(df)



