def Hello_world_function(name):
    print("Hello World "+ str(name))

def Get_username(question):
    username=input(str(question)+"\n")
    return username

Name=Get_username("What is your name?")

Hello_world_function(Name)