def force_evaluation(m1,m2,r):
    G=6.67408e-11
    F=G*m1*m2/(r**2)
    return F
    
def acceleration_evaluation(m1,m2,F):
    a1=F/m1
    a2=F/m2
    return a1, a2
    
def find_time():
    m1=100000000
    m2=50000000
    r=300
    
    F=force_evaluation(m1,m2,r)
    a1,a2=acceleration_evaluation(m1,m2,F)
    delta=10000000000000000000000000
    t=0
    tr=0
    while t<=100000:

        if abs(0.5*a1*t**2+0.5*a2*t**2-r)<delta:
            delta=abs(0.5*a1*t**2+0.5*a2*t**2-r)
            tr=t
            
        t+=1
    return tr
tr=find_time()
print(tr)
    
    