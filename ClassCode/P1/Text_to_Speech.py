# pip install pyttsx3

import pyttsx3
engine = pyttsx3.init()


msg='Hello World!'
engine.say(msg)
engine.setProperty('rate', 20) #make it speak slow/fast
engine.runAndWait() #run and do not close immediately