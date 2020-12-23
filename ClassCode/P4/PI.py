#Leibniz formula
pi_div4=0
k=0
while k<100000:
    pi_div4+= ((-1)**k) / (2*k+1)
    
    print(pi_div4*4)
    k+=1
pi=pi_div4*4
print(pi)

