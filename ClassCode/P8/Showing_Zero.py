import numpy as np

y=[-1,0,-1,0,-1,0,-1,1]
c=np.array(['Negative One' if x==-1 else 'Zero' if x==0 else 'One' if x==1 else "" for x in y])
#no elif
#else if
d=c[c=="Zero"]
print(d)

