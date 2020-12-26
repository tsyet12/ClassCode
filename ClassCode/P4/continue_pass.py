list=[1,2,3,4,5,6,7,8,9,10]

for i in list:
    if i==7:
        print("pass")
        pass
    print(i)
    
print("Now we try using continue")
for i in list:
    if i==7:
        print("continue")
        continue
    print(i)