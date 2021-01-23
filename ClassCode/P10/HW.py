import pandas as pd
path=r'C:\Users\User\Desktop\Class\ClassCode\P10\\'
df=pd.read_csv(path+"iris.csv")
index=df.loc[df['variety']=="Virginica"].index
df.drop(index, inplace=True)
df["petal.area"]=df["petal.length"]*df["petal.width"]
df['sepal.area']=df["sepal.length"]*df["sepal.width"]

Setosa=df.loc[df['variety']=="Setosa"]
Versicolor=df.loc[df['variety']=="Versicolor"]

print("Setosa: ", Setosa.mean()["petal.area"]+Setosa.mean()["sepal.area"])
print("Versicolor: ", Versicolor.mean()["petal.area"]+Versicolor.mean()["sepal.area"])



