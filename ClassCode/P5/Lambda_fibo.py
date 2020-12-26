x=[1,1]
f = lambda x: x+[x[-1]+x[-2]]

for i in range(101):
    x=f(x)
    
print(x)