from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome("chromedriver")

 

driver.get("https://web.whatsapp.com")

def msg():
    name = input("/nEnter Group or username: ")
    message = input("Enter your message here")
    Count = int(input("Enter the message count: "))


    #Finding whom to message
    user = driver.find_element_by_xpath(
        '//span[@title = "{}"]'.format(name)
    )
    user.click()

    text_box = driver.find_element_by_class_name("_1Plpp")
  

    driver.maximize_window() # For maximizing window



    #send button
    for i in range(Count):
        text_box.send_keys(message + Keys.ENTER)

        driver.implicitly_wait(5)
        # driver.find_element_by_class_name("_3HQNh _1Ae7k").click()
        # driver.find_element_by_class_name("_4sWnG").click()
        

msg()

def reps():
    print("do you want to send more message to anyone")
    askUser = input("Press y for Yes and n for No")
    if(askUser== 'y' or askUser== 'Y'):
        msg()
        reps()
    elif(askUser== 'N' or askUser == 'n'):
        print("exited")
    else:
        print("enter something valid")
        reps()
reps()

   



     