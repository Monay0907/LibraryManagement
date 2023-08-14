import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
import mysql.connector
from usermainpage import *

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="monay",
    database="mydatabase"
)
mycursor = mydb.cursor()

# Function to handle user login
def signin():
    gmail = tx1.get()
    password = tx2.get()
    sql_Query = "SELECT * FROM login WHERE email = %s AND password = %s"
    mycursor.execute(sql_Query, (gmail, password))
    myresult = mycursor.fetchone()
    if myresult is None:
        messagebox.showerror("Invalid", "Wrong details\nNot registered? Register")
    else:
        messagebox.showinfo("Login", "Login successful")
        makewindow(gmail)

# Function to open the forget password window
def forget():
    rootwindow.destroy()
    import forgetpass_user

# Function to open the registration window
def register():
    rootwindow.destroy()
    import register

# Function to go back to the main homepage
def back():
    rootwindow.destroy()
    import mainhomepage

# Main window setup
rootwindow = tk.Tk()
rootwindow.title("USER SIGN IN")
rootwindow.geometry('600x400')
rootwindow.resizable(False, False)
rootwindow.configure(bg="LemonChiffon2")

# Title and subtitle
title_font = ("Arial", 24, "bold")
subtitle_font = ("Arial", 16)

lb1 = tk.Label(rootwindow, text="LIBRARY LOGIN", font=title_font, bg="LemonChiffon2")
lb1.pack(pady=20)

lb2 = tk.Label(rootwindow, text="SIGN IN TO CONTINUE", font=subtitle_font, bg="LemonChiffon2")
lb2.pack()

# Frame for login fields
frame = tk.Frame(rootwindow, width=500, height=500, borderwidth=25, bg="LemonChiffon2")
frame.pack(anchor=tk.CENTER)

lf1 = tk.Label(frame, text="Email Id", width=15, font=("Arial", 12), bg="LemonChiffon2")
lf1.grid(row=0)
tx1 = tk.Entry(frame, width=25, font=("Arial", 12))
tx1.grid(row=0, column=2, padx=10)

lf2 = tk.Label(frame, text="Password", width=15, font=("Arial", 12), bg="LemonChiffon2")
lf2.grid(row=1)
tx2 = tk.Entry(frame, width=25, show="*", font=("Arial", 12))
tx2.grid(row=1, column=2, padx=20, pady=20)

# Sign in button
signin_button = tk.Button(frame, text="Sign in", command=signin, width=15, font=("Arial", 14, "bold"))
signin_button.grid(row=2, columnspan=4, pady=10)

# Forget password button
forget_button = tk.Button(frame, text="Forget password", command=forget, width=20, font=("Arial", 14,"bold"))
forget_button.grid(row=3, columnspan=4, pady=10)

# Register button
register_button = tk.Button(frame, text="Register", command=register, width=15, font=("Arial", 14,"bold"))
register_button.grid(row=4, columnspan=4, pady=10)

# Back button
back_button = tk.Button(frame, text="BACK", command=back, width=15, font=("Arial", 14, "bold"))
back_button.grid(row=5, columnspan=4, pady=20)

# Main loop
rootwindow.mainloop()
