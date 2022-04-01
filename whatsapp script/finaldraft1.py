# importing the module
import pywhatkit as kit
import csv
import time
 
# using Exception Handling to avoid
# unprecedented errors
# def msg():
#     name = input("/nEnter Group or username: ")
#     message = input("Enter your message here")
#     Count = int(input("Enter the message count: "))

file_numbers = input("enter the name of the files with numbers: ")
file = open(file_numbers, "r")
csv_reader = csv.reader(file)

lists_from_csv = []

for row in csv_reader:
    lists_from_csv.append(row)

print(lists_from_csv)

msg = input("enter the message you want to send: ")

time_hour = int(input("Enter the hour you want to send the message at: "))
time_min = int(input("Enter the minute you want to send the message at: "))

for number in lists_from_csv:

    
    string_number = str(number)
    
    try:    
        # sending message to receiver
        # using pywhatkit
        kit.sendwhatmsg(string_number,
                                msg,
                                time_hour, time_min, 2, True, 2)
        print("Successfully Sent!")

        time_min = time_min + 1
        
    except:
        
        # handling exception
        # and printing error message
        print("An Unexpected Error!")


 
