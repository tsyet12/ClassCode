class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        print(self.a+self.b)
    
    def substraction(self):
        print(self.a-self.b)
        
    def multiplication(self):
        print(self.a*self.b)
        
    def division(self):
        print(self.a/self.b)

cal=calculator(a=1,b=2)

cal.addition()

