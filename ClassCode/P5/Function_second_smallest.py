def second_smallest(list1,list2):
    x=list1+list2
    smallest=999999999999
    second_small=9999999999
    for i in x:
        if i<smallest and i%2!=0:
            second_small=smallest
            smallest=i
        elif i>smallest and i<second_small and i%2!=0:
            second_small=i
    return second_small
'''
def second_smallest2(list1,list2):
    x=list1+list2
    x_min=99999999999
    x_min2=99999999999
    for i in range(len(x)+1):
        if min(x)%2==0: #even 
            x.remove(min(x))
        elif min(x)!=0: #odd
            x_min2=x_min
            x_min=min(x) #replace
            x.remove(min(x))      
            
    return x_min2
    
'''
Y=second_smallest([1,3,5,2] ,[9,2,9,4,3])
print(Y)
