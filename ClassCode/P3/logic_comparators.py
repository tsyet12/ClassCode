X=1234567890.1234
X=int(X) #1234567890
X=str(X)[-1]  #"0"
X=int(X)  #0
condition=(X<=6 and X>=1)and X%2!=0  #it is odd

print(condition)