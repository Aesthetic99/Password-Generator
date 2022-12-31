from tkinter import *
from pyperclip import copy
from string import ascii_letters, punctuation, digits
from random import randint

def generate():
    char = ascii_letters + punctuation + digits
    char_list = list (char)
    password = ""
    i = 1
    while i<=12:
        if password == "":
            password = char_list[randint(0,len(char_list)-1)]
        else:
            password = password + char_list[randint(0,len(char_list)-1)]

        i+= 1
    
    copy(password)

    

root = Tk()
root.geometry("400x80")

generate_button = Button (text="Generate", command=generate)
generate_button.pack()

footer_label = Label(text="Developed with Love by EJ", bg="cyan" ,fg="black", font="comicsans 19 italic" ,borderwidth=3 )
footer_label.pack(side=BOTTOM, fill=X)

root.mainloop()
