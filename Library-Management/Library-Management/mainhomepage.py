#firstpage
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="monay",
    database="mydatabase"
)
mycursor = mydb.cursor()
# Function to open student login window
def open_student_login():
    rootwindow.destroy()
    import login
# Function to open admin login window
def open_admin_login():
    rootwindow.destroy()
    import admin
# Main window setup
rootwindow = tk.Tk()
rootwindow.title("Library Management System")
rootwindow.geometry('600x400')
rootwindow.resizable(False, False)
rootwindow.configure(bg="LemonChiffon2")
# Load and display the image
image = Image.open("D:\programs\python\library.jpg")
test = ImageTk.PhotoImage(image)
lb1 = tk.Label(rootwindow, image=test, bg="LemonChiffon2")
lb1.pack(pady=20)
# Label and Buttons
heading_font = ("Arial", 24, "bold")
label_font = ("Arial", 16)
lb2 = tk.Label(rootwindow, text="Welcome to the Library", font=heading_font, bg="#f0f0f0")
lb2.pack()
frame_buttons = tk.Frame(rootwindow, bg="LemonChiffon2")
frame_buttons.pack(pady=20)
bt1 = tk.Button(frame_buttons, text="USER", command=open_student_login, width=15, font=label_font)
bt1.pack(side=tk.LEFT, padx=20)
bt2 = tk.Button(frame_buttons, text="ADMIN", command=open_admin_login, width=15, font=label_font)
bt2.pack(side=tk.LEFT, padx=20)
# Start the main event loop
rootwindow.mainloop()
