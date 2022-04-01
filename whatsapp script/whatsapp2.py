from selenium import webdriver

driver = webdriver.Chrome("chromedriver")

driver.get("https://web.whatsapp.com")

def reps():
    print("Do you want to send more msg to anyone")
    askUser = input("Press y for Yes and n for No : ")
    if (askUser == 'Y' or askUser == 'y'):
        msg()
    elif (askUser == 'N' or askUser == 'n'):
        print("Thank you see you soon")
    else:
        print("Please Enter Valid option :\n")
        reps()

def msg():
    name = input('\nEnter Group/User Name: ')
    message = input("Enter your message to group/user: ")

    # Find Whom to message     
    try:
        Count = int(input("Enter the message count:"))
        
        user = driver.find_element_by_xpath(
        '//span[@title = "{}"]'.format(name))
        user.click()
    except:
        msg()

    text_box = driver.find_element_by_class_name('p3_M1')

    # driver.maximize_window() # For maximizing window
    # driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

    #Send Button
    for i in range(Count):
        text_box.send_keys(message)
        driver.maximize_window() # For maximizing window
        driver.implicitly_wait(10) # gives an implicit wait for 20 seconds
        driver.find_element_by_class_name("_4sWnG").click()
    
    reps()

msg()