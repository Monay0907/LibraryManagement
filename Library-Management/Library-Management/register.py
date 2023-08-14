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
rootwindow.title("Registration form")
rootwindow.geometry('500x500')
rootwindow.resizable(False, False)
rootwindow.configure(bg="LemonChiffon2")
lb1=Label(rootwindow,text="REGISTER")
lb1.pack()
# lb2=Label(rootwindow,text="SIGN IN TO CONTINUE")
# lb2.pack()
frame=tk.Frame(rootwindow, width=300, height=300,borderwidth=25,bg="LemonChiffon2")
frame.place(x=150,y=100)
# lb3=Label(frame, text="I am inside a Frame", font='Arial 17 bold')
# lb3.grid(row=0)
#creating inside the frame
lf1=Label(frame,text="First Name",justify='left')
lf1.grid(row=1)
tx1=tk.Entry(frame,width=10,justify='left')
tx1.grid(row=1,column=1,pady=15)
lf2=Label(frame,text="Last Name",justify='left')
lf2.grid(row=2)
tx2=Entry(frame,width=10)
tx2.grid(row=2,column=1)
lf3=Label(frame,text="Email ID",justify='left')
lf3.grid(row=3)
tx3=Entry(frame,width=10)
tx3.grid(row=3,column=1)
lf4=Label(frame,text="Mobile Number",justify='left')
lf4.grid(row=4)
tx4=Entry(frame,width=10)
tx4.grid(row=4,column=1)
lf5=Label(frame,text="Address",justify='left')
lf5.grid(row=5)
tx5=tk.Entry(frame,width=10,bd=3)
tx5.grid(row=5,column=1)
#creating password field
lf6=Label(frame,text="Password",justify='left')
lf6.grid(row=6)
tx6=tk.Entry(frame,width=10,bd=3)
tx6.grid(row=6,column=1)
#confirm password
lf7=Label(frame,text=" Confirm Password",justify='left')
lf7.grid(row=7)
tx7=tk.Entry(frame,width=10,bd=3)
tx7.grid(row=7,column=1)


#creating Submit button
#creating function

def verify():
    error=0
    fname=tx1.get()
    if(len(fname.strip())==0):
      error=1
      messagebox.showerror("showerror", "Name cannot be empty")
    lname=tx2.get()
    if(len(lname.strip())==0):
      error=1
      messagebox.showerror("showerror", "Name cannot be empty")
    mail=str(tx3.get())
    if(len(mail.strip())==0):
      error=1
      messagebox.showerror("showerror", "mail cannot be empty")
    #if mail already in database
    mailid=[]
    mailid.append(mail)
    query="select * from login where email =%s"
    mycursor.execute(query,(mailid))
    myresult = mycursor.fetchone()
    if myresult!=None:
        error=1
        messagebox.showerror("showerror", "mail already in use")
        ######################################################
    mob=tx4.get()
    if(len(mob.strip())==0 or len(mob)>10):
      error=1
      messagebox.showerror("showerror", "Invalid mobile number")
      ########################################################## if phone already in use
    nonum=[]
    nonum.append(mob)
    mycursor2=mydb.cursor()
    query="select * from login where phone_num =%s"
    mycursor2.execute(query,nonum)
    myresult = mycursor2.fetchone()
    if myresult!=None:
        error=1
        messagebox.showerror("showerror", "mobile already in use")
    addres=tx5.get()
    if(len(addres.strip())==0):
      error=1
      messagebox.showerror("showerror", "Address cannot be empty")
    pw=tx6.get()
    cpw=tx7.get()
    if(pw!=cpw):
        messagebox.showerror("showerror", "Password does not match")
        error=1
    if(error==0):
      sql = "INSERT INTO login (first_name,last_name,email,password,address,phone_num) VALUES (%s, %s,%s,%s,%s,%s)"
      val = (fname,lname,mail,pw,addres,mob)
      mycursor.execute(sql, val)
      mydb.commit()
      messagebox.showerror("register", "success")
      rootwindow.destroy()
      import login
#-----------------
submit=Button(frame,text="Submit",command=verify)
submit.grid(row=8,columnspan=4)
def back():
    rootwindow.destroy()
    import login
backbutton=tk.Button(frame,text="BACK",command=back)
backbutton.grid(row=10,columnspan=4,pady=20)


rootwindow.mainloop()
