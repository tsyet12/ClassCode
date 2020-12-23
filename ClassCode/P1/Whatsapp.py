#pip install selenium, pywin32
#download geckodriver https://github.com/mozilla/geckodriver/releases
#geckodriver: extract and put it in your Python directory eg. C:\Users\User\AppData\Local\Programs\Python\Python37
#run as administrator

#Let's import the Selenium package
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

text='sent from python bot'
contact='Python Course'
ff_profile_dir = r"C:\Users\User\Desktop\Class\ClassCode\P1" #current file location



ff_profile = webdriver.FirefoxProfile(profile_directory=ff_profile_dir)
web = webdriver.Firefox(ff_profile)
web.get('http://web.whatsapp.com')
time.sleep(25)

elem = web.find_element_by_xpath("//span[@title='{}']".format(contact))
elem.click()

input_box = web.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]') #check xpath 
input_box.send_keys(text + Keys.ENTER)
time.sleep(2)