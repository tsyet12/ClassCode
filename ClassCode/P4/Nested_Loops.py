#Nested Loops

X=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

for i in range(3): #len(X[0])
    for j in range(4): #len(X)
        if X[j][i]%2==0 and X[j][i]%3!=0: #even and not div 3
            X[j][i]="even"
        elif X[j][i]%2==1 and X[j][i]%3!=0: #odd and not div 3
            X[j][i]="odd"
print(X)
                
