class Hello_bot:
    def __init__(self, name):
        self.name=name
        
    def say_hello(self):
        print("Hello World! My name is", self.name)


class Hello_Goodbye_Bot(Hello_bot):
    def __init__(self,name):
        Hello_bot.__init__(self, name)
        self.name=name
    def say_goodbye(self):
        print("Goodbye World! My name is", self.name)
'''        
#bot=Hello_bot(name="Alan Turing")        
bot=Hello_Goodbye_Bot(name="Alan Turing")
bot.say_hello()
bot.say_goodbye()
'''