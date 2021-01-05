class parent:
    def __init__(self):
        print("init parent")
        
    def function_A(self):
        print("function_A")
        
        
class child(parent):
    def __init__(self):
        parent.__init__(self)
        print("init child")
    def function_B(self):
        print("function B")
        
c=child()
c.function_A()
c.function_B()


