import pandas as pd

path=r"C:\Users\User\Desktop\Class\ClassCode\P9\\"
df = pd.read_excel(path+"Duplicate.xlsx")

df=df.drop_duplicates()
df=df.sort_values("Energy")

cost=df.iloc[-1,-1]
print(df)
print(cost)
