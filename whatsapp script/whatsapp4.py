from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import json

driver = webdriver.Chrome("chromedriver")
driver.get("https://web.whatsapp.com")

#Uses python3
#This function when called will open up WhatsApp Web on the chrome and create a wait object.
def call_chrome():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://web.whatsapp.com")
    wait= WebDriverWait(driver , 10)
    return driver,wait
#Uses python3
#This function when called will open the receiver you want to message.
def target_naive():
    target=input('Enter the name of person')
    target=json.dumps(target)
    #Here json is used because we need name as '"Kapil"'(string to be
    #enclosed withing quotes)
    x_arg='//span[contains(@title, '+target+')]'
    target=wait.until(EC.presence_of_element_located((By.XPATH , x_arg)))
    target.click()
#Uses python3
#This will select the input box.
def send_msg():
    string=input('Enter the message')
    input_box = driver.find_element_by_class_name('p3_M1')
    n=int(input('No. of times the message should be send'))
    for i in range(n):
        input_box.send_keys(string+Keys.ENTER)
#Keys.ENTER will press enter key after writing name of the target.


#Uses python3
#Run this block at the end to send the message.
driver,wait = call_chrome()
target_naive()
send_msg()