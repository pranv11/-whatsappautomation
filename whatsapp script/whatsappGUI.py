from tkinter import *

window = Tk()


def message_file():
    print(e1_value.get())
    miles = int(e1_value.get())*1.6006
    t1.insert(END, miles)

#making a button
b1 = Button(window, text="Message", command=message_file)
b1.grid(row=0,column=0,rowspan=3)


#entry
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

#text widget
t1 = Text(window,height=1, width=10)
t1.grid(row=0,column=2)

window.mainloop()