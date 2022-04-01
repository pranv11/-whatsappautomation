# importing the module
import pywhatkit as kit
import time
 
# using Exception Handling to avoid
# unprecedented errors
# def msg():
#     name = input("/nEnter Group or username: ")
#     message = input("Enter your message here")
#     Count = int(input("Enter the message count: "))
msg = input("enter the message you want to send")
while True:
  number = input("enter a number")
  
  if number!= "end":

    try:
   
  # sending message to receiver
  # using pywhatkit
      kit.sendwhatmsg(number,
                        msg,
                        21, 34)
      print("Successfully Sent!")
 
    except:
   
  # handling exception
  # and printing error message
      print("An Unexpected Error!")
    
    continue
  else:
    print("thank you! ")
    break

