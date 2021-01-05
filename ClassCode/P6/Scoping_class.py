on=True

class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        print(self.a+self.b)
    
    def substraction(self):
        print(self.a-self.b)
        if self.b==0:
            self.turn_off()
    def multiplication(self):
        print(self.a*self.b)
        
    def division(self):
        print(self.a/self.b)
        
    def turn_off(self):    
        global on
        on=False

cal=calculator(a=1,b=0)
cal.substraction()
if on==True:
    cal.division()