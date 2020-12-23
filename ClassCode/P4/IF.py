x=input("Give me a integer \n")
int(x)
if x<2: #Error instead of False. Program fails
    print("x is smaller than two")
elif x>30:
    print("x is bigger than 30")
else:
    print("x is between 2 and 30")

