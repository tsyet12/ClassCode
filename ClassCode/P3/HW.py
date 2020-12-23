name=["Mark","Lee", "Rac", "Qi","Alan","Dog","Pikachu"]
mark=[95,10,32,33,80,60,30]
age=[60,15,3,70,13,1,0.5]



d1=dict(zip(name,mark))
d2=dict(zip(age,mark))
name.sort(key=d1.get)
age.sort(key=d2.get)
mark.sort()
mark.reverse()

top=int(len(name)*0.8)

first_ans=name[top-1]


print(top)
print(name)

print(first_ans)


print((1<=age[top]<=15) and age[top+1]>age[top])