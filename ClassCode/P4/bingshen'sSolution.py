
X=[14,23,4,2,9,13]
new=[]
while X:
    min = X[0]  
    for i in X: 
        if i < min:
            min = i
    new.append(min)
    X.remove(min)    
 
print(new)