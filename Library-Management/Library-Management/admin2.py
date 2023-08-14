import tkinter as tk
import smtplib
from email.mime.text import MIMEText
from tkinter.ttk import *
import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="monay",
    database="mydatabase"
)
mycursor = mydb.cursor()

rootwindow = tk.Tk()
rootwindow.title("Admin")
rootwindow.geometry('500x500')
rootwindow.resizable(False, False)
rootwindow.configure(bg="LemonChiffon2")

l3 = Label(rootwindow, text="")
l3.pack()

def sendreminder():
    sender = 'admin@example.com'
    port = 1025
    
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")

    query = "select email from reminder where returning_date = %s and status = 'no'"
    mycursor.execute(query, (date,))  
    myresult = mycursor.fetchall()
    
    if not myresult:
        msg1 = f"No reminder mail to be sent for {date}"
        l3.configure(text=msg1)
    else:
        receivers = [result[0] for result in myresult] 
        msg = MIMEText("Dear user, Today is the last date of submission of books.\nFailing which due fees will be collected.")
        msg['Subject'] = 'Mail regarding submission of books'
        msg['From'] = 'admin@example.com'
        msg['To'] = ", ".join(receivers)
        
        with smtplib.SMTP('localhost', port) as server:
            server.sendmail(sender, receivers, msg.as_string())
            msg = f"Success! Reminder mail is sent for {date}"
            l3.configure(text=msg)

lb1 = Label(rootwindow, text="Welcome Admin. Send reminder")
lb1.pack()

reminder = Button(rootwindow, text="Send Reminder", command=sendreminder)
reminder.pack(pady=10)

def back():
    rootwindow.destroy()
    import admin

backbutton = tk.Button(rootwindow, text="BACK", command=back)
backbutton.pack(pady=20)

rootwindow.mainloop()
#---------------------------------------------------------------------------------------------------
# first form the server 
# run on terminal following command 
# python -m smtpd -c DebuggingServer -n localhost:1025
# --------------------------------------------------------------------------------------------------- 
