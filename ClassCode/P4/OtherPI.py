#Leibniz formula
pi_div4=0
k=0
while k<100000:
    pi_div4+= ((-1)**k) / (2*k+1)
    k+=1
pi=pi_div4*4
print(pi)

k=1
n=10000
mod_pi=0
while k<n:
    mod_pi+=n%k
    k+=1

mod_pi=((1-mod_pi/n**2)*12)**0.5
print(mod_pi)


k=0
n=10000
B_pi=0
while k<n:
    B_pi+=1/(16**k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
    k+=1
print(B_pi)

