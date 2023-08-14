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
rootwindow.title("Reset Password")
rootwindow.geometry('500x500')
rootwindow.resizable(False, False)
rootwindow.configure(bg="LemonChiffon2")
lb1=tk.Label(rootwindow,text="Reset Password")
lb1.pack()
frame=tk.Frame(rootwindow, width=800, height=500,borderwidth=25,bg="LemonChiffon2")
frame.pack()
#creating inside frame
lf1=tk.Label(frame,text="Enter Email Id",width=10)
lf1.grid(row=0)
tx1=tk.Entry(frame,width=20)
tx1.grid(row=0,column=2,padx=10)
#another field
lf2=tk.Label(frame,text="Enter New Password",width=20)
lf2.grid(row=1)
tx2=tk.Entry(frame,width=20)
tx2.grid(row=1,column=2,padx=10,pady=10)
def reset():
    email=tx1.get()
    nmail=[]
    nmail.append(email)
    newpass=tx2.get()
    query = "select * from login where email =%s" ################################3
    mycursor.execute(query,(nmail))
    myresult = mycursor.fetchone()
    if myresult==None:
        messagebox.showerror("Reset Password","Email Does Not Exist")
    else:
        subquery="Update login set password=%s WHERE email=%s"
        mycursor.execute(subquery,(newpass,email))
        mydb.commit()
        messagebox.showinfo("Reset Password", "success")
        # rootwindow.destroy()
        # import login
bt1=tk.Button(frame,text="Confirm",command=reset)
bt1.grid(row=2,columnspan=3)
def back():
    rootwindow.destroy()
    import login
backbutton=tk.Button(frame,text="BACK",command=back)
backbutton.grid(row=3,columnspan=4,pady=20)
####################
rootwindow.mainloop()