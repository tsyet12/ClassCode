import pandas as pd

data=[["Hello",2,3],[4,"World",6],[7,8,"Pandas"]]

df = pd.DataFrame (data, columns = ['A','B', 'C'], index=['First', 'Second', 'Third'])


str1= df.iloc[0,0]
str2= df.iloc[1,1]
str3= df.iloc[2,2]

print(str1, " ",str2," ", str3)