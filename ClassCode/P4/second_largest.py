X=[16,1,2,3,4,5,6,7,8,11,12,13,14,15]

largest=0
second_larg=0

for i in X:
    if i>largest:
        second_larg=largest
        largest=i
    elif i<largest and i>second_larg:
        second_larg=i
print(second_larg)