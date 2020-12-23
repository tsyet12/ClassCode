X=[[2,3,4] , [7,8,9], [4,5,6], [10,11,12]]
max=0
for i in range(4):
    for j in range(3):
        if X[i][j]%4!=0:
            for z in range(1,X[i][j]-1): #check prime (divisibility)
                if X[i][j]%z==0 and z!=1: #not prime
                    if X[i][j]>max: #replace max if it is bigger
                        max=X[i][j]

print(max)