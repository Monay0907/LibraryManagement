import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="monay",
  database="mydatabase"
)
mycursor = mydb.cursor()
rootwindow=tk.Tk()
rootwindow.title("Admin")
rootwindow.geometry('500x500')
rootwindow.resizable(False, False)
rootwindow.configure(bg="LemonChiffon2")
lb1=Label(rootwindow,text="ADMIN LOGIN")
lb1.pack()
frame=tk.Frame(rootwindow, width=800, height=500,borderwidth=25,bg="LemonChiffon2")
frame.pack()
#creating inside frame
lf1=tk.Label(frame,text="User Name",width=10)
lf1.grid(row=0)
tx1=tk.Entry(frame,width=20)
tx1.grid(row=0,column=2,padx=10)
#another field
lf2=tk.Label(frame,text="Password",width=10)
lf2.grid(row=1)
tx2=tk.Entry(frame,width=20)
tx2.grid(row=1,column=2,padx=10,pady=10)
def signin():
    gmail=tx1.get()
    password=tx2.get()
    sql_Query = "select * from admin where user =%s and password=%s" ################################3
    mycursor.execute(sql_Query,(gmail,password))
    myresult = mycursor.fetchone()
    if myresult==None:
        messagebox.showerror("invalid", "Wrong credentials")
    else:
        messagebox.showinfo("login", "success")
        rootwindow.destroy()
        import admin2
signin=tk.Button(frame,text="Sign in",command=signin)
signin.grid(row=2,columnspan=4)
def back():
    rootwindow.destroy()
    import mainhomepage
backbutton=tk.Button(frame,text="BACK",command=back)
backbutton.grid(row=3,columnspan=4,pady=20)
rootwindow.mainloop()




















rootwindow.mainloop()