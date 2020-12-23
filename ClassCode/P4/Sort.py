x=[14,23,4,2,9,13]
n = len(x) 

#bubble sort
for i in range(n-1): 
    for j in range(0, n-i-1): 
        if x[j] > x[j+1] : 
            x[j], x[j+1] = x[j+1], x[j] 
