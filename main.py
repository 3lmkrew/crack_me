# Brute force password cracker
# By: Mason Hernandez
# 03/09/2022

from brute_force import brute_force
from tkinter import *


gui_window = Tk()
gui_window.config()
gui_window.geometry("600x400")
gui_window.title("Let's get Cracking")
gui_window.iconbitmap("fav.ico")

# IMAGES
lock_image = PhotoImage(file="password.png")
hacker_image = PhotoImage(file="hacker.png")

# CANVAS
lock_canvas = Canvas(width=200, height=200)
lock_canvas.create_image(128, 128, image=lock_image)
lock_canvas.place(x=395, y=0)

hacker_canvas = Canvas(width=200, height=200)
hacker_canvas.create_image(128,128, image=hacker_image)
hacker_canvas.place(x=220, y=190)
# LABELS
title_label = Label(text="Mason's Brute Force Password Cracker")
title_label.config(fg="#2D31FA", font="14")
title_label.place(x=110, y=20)

secret_password_label = Label(text="Type a secret Password:")
secret_password_label.place(x=50, y=100)

found_answer_label = Label(text="The secret password is:")
found_answer_label.place(x=50, y=180)

attempts_label = Label(text="Attempts:")
attempts_label.place(x=75, y=300)

attempts_answer_label = Label(text=f"")
attempts_answer_label.place(x=150, y=300)

time_label = Label(text="Time in Seconds:")
time_label.place(x=40,y=350)

time_answer_label = Label(text="")
time_answer_label.place(x=150, y=350)



# ENTRY'S
secret_password_entry = Entry()
secret_password_entry.config(width=20, show="*")
secret_password_entry.place(x=200, y=100)

found_answer_entry = Entry()
found_answer_entry.config(width=20)
found_answer_entry.place(x=200, y=180)


# BUTTON LOGIC
def search():
    password_input = secret_password_entry.get()
    code, attempts, distance = brute_force(password_input)
    print(f"The secret password is: {code}, it took {attempts} attempts, in {distance} seconds ")
    found_answer_entry.insert(END, code)
    attempts_answer_label.config(text=f"{attempts}")
    time_answer_label.config(text=f"{distance}")

def clear_all():
    secret_password_entry.delete(0, END)
    found_answer_entry.delete(0, END)
    attempts_answer_label.config(text="")
    time_answer_label.config(text="")

# BUTTONS
search_button = Button()
search_button.config(width=10, text="SEARCH", bg="#FFC300",command=search)
search_button.place(x=350, y=95)

clear_button = Button()
clear_button.config(width=10, text="CLEAR ALL", bg="lightblue", command=clear_all)
clear_button.place(x=500, y=355)





gui_window.mainloop()

