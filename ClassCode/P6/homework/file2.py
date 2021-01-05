from file1 import simple_calculator as sc
import math
class better_calculator(sc):
    def __init__(self,a,b):
        sc.__init__(self,a,b)
        self.a=a
        self.b=b
    def sin_ab(self):
        return math.sin(self.a/self.b)
    def cos_ab(self):
        return math.cos(self.a/self.b)
    def tan_ab(self):
        return math.tan(self.a*self.b)
    def pi_ab(self):
        return math.pi*self.a*self.b

bc=better_calculator(a=1,b=30)
ans=bc.tan_ab()
print(ans)