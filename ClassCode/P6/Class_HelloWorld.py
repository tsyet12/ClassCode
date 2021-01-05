class Hello_bot:
    def __init__(self, name):
        self.name=name
        
    def say_hello(self):
        print("Hello World! My name is", self.name)

Bot=Hello_bot(name="Alan Turing")
Bot.say_hello()