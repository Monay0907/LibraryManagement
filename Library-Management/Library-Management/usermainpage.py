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
mycursor2 = mydb.cursor()
mycursor3 = mydb.cursor()
mycursor4 = mydb.cursor()
def makewindow(m):
    mail=[]
    mail.append(m)
    rootwindow1=tk.Tk()
    rootwindow1.title("USER SIGN IN")
    rootwindow1.geometry('500x500')
    rootwindow1.resizable(False, False)
    rootwindow1.configure(bg="LemonChiffon2")
    frame=tk.Frame(rootwindow1, width=500, height=500,borderwidth=25,bg="LemonChiffon2")
    frame.pack(anchor=tk.CENTER)
    lb1=tk.Label(frame,text="WELCOME")
    lb1.grid(row=0,column=0)
    query1="select first_name from login where email=%s"
    mycursor.execute(query1,(mail))
    myresult = mycursor.fetchone()
    query2="select last_name from login where email=%s"
    mycursor2.execute(query2,(mail))
    myresult2 = mycursor2.fetchone()
    lb2=tk.Label(frame,text=myresult)
    lb2.grid(row=0,column=1)
    lb3=tk.Label(frame,text=myresult2)
    lb3.grid(row=0,column=2)
    def mybooks():
        query3="select book1 from books_taken where email=%s"
        mycursor3.execute(query3,(mail))
        r1=mycursor3.fetchone()
        query4="select book2 from books_taken where email=%s"
        mycursor4.execute(query4,(mail))
        r2=mycursor4.fetchone()
        if(r1!=None or r2!=None):
            l1=tk.Label(frame,text=r1)
            l1.grid(row=1,column=2)
            l2=tk.Label(frame,text=r2)
            l2.grid(row=1,column=3)
    mb=tk.Button(frame,text="SHOW MY BOOKS",command=mybooks)
    mb.grid(row=1,column=0)
    def back():
        rootwindow1.destroy()
        # import login
    backbutton=tk.Button(frame,text="BACK",command=back)
    backbutton.grid(row=3,columnspan=4,pady=20)
    ##################
    rootwindow1.mainloop()
   
















######################
