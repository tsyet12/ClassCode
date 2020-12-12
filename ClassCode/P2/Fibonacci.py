x=[1,1]

for i in range(1000):
    x=x+[x[-1]+x[-2]]
    #iteration 1
    #x=[1,1]+[1+1]
    #x=[1,1]+[2]
    #x=[1,1,2]
    #iteration 2
    #x=[1,1,2]+[1+2]
    #x=[1,1,2]+[3]
    #x=[1,1,2,3]
print(x)

print(x[-1]/x[-2])