def gravity_force(M):
    g=9.81
    W=M*g
    return W

def drag_force(Cd,r,M,V):
    pi=3.1415926535
    A=2*pi*(r**2)
    D=Cd*r*(V**2)*A/2
    return D

def iterative_evaluation():
    V=0
    Vt=0
    delta=100000000 #some large number
    while V<=100:
        if abs(gravity_force(M=2)-drag_force(Cd=0.3,r=1,M=2,V=V))<delta:
            delta=abs(gravity_force(M=2)-drag_force(Cd=0.3,r=1,M=2,V=V))
            Vt=V
        V+=0.1
    return Vt

Vt= iterative_evaluation()

print("iterative Vt : ",Vt)



def analytical_check(M,Cd,r):
    pi=3.1415926535
    A=2*pi*(r**2)
    W=gravity_force(M)
    Vt=((2*W)/(Cd*r*A))**0.5
    return Vt

Vt2=analytical_check(M=2,Cd=0.3,r=1)

print("analytical Vt : ",Vt)
