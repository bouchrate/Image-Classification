from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
# Functionality Part

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    termsandconditions.set(0)

def connect_database():
    if emailEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or confirmEntry.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')

    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')

    elif check.get() == 0:
        messagebox.showerror('Error', 'Please Accept Terms & Conditions')

    else:
        try:
            con = pymysql.connect(
                host="localhost",
                user="bouchra",
                password="2000boubou@"
            )
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again')
            return

        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key not null, email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)

        except:
            mycursor.execute('use userdata')
        query = 'select * from data where username=%s'
        mycursor.execute(query, (usernameEntry.get()))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showinfo('Error', 'Username Already Exists')

        else:
            query = 'insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is successful')
            clear()
            signup_window.destroy()
            import signin


def login_page():
    signup_window.destroy()
    import signin





# GUI Part
signup_window = Tk()
signup_window.geometry('990x660+50+50')
signup_window.resizable(0, 0)
signup_window.title('Login Page')

bgImage = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(signup_window, image=bgImage)
bgLabel.place(x=0, y=0)

frame= Frame(signup_window, bg='white')
frame.place(x=554,y=100)

heading = Label(frame, text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light', 18, 'bold'), bg='white',
                fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)

emaillabel = Label(frame, text='Email',font=('Microsoft Yahei UI Light', 10, 'bold'),bg='white',fg='firebrick1')
emaillabel.grid(row=1, column=0, sticky='w', padx= 25, pady=(10,0))

emailEntry = Entry(frame, width=30, font=('Microsoft Yeahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
emailEntry.grid(row=2, column=0, sticky='w', padx=25)

usernamelabel = Label(frame, text='Username',font=('Microsoft Yahei UI Light', 10, 'bold'),bg='white',fg='firebrick1')
usernamelabel .grid(row=3, column=0, sticky='w', padx= 25, pady=(10,0))

usernameEntry = Entry(frame, width=30, font=('Microsoft Yeahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
usernameEntry.grid(row=4, column=0, sticky='w', padx=25)


passwordlabel = Label(frame, text='Password',font=('Microsoft Yahei UI Light', 10, 'bold'),bg='white',fg='firebrick1')
passwordlabel.grid(row=5, column=0, sticky='w', padx= 25, pady=(10,0))

passwordEntry = Entry(frame, width=30, font=('Microsoft Yeahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
passwordEntry.grid(row=6, column=0, sticky='w', padx=25)

confirmlabel = Label(frame, text='Confirm password',font=('Microsoft Yahei UI Light', 10, 'bold'),bg='white',fg='firebrick1')
confirmlabel.grid(row=7, column=0, sticky='w', padx= 25, pady=(10,0))

confirmEntry = Entry(frame, width=30, font=('Microsoft Yeahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
confirmEntry.grid(row=8, column=0, sticky='w', padx=25)

check = IntVar()
termsandconditions = Checkbutton(frame,text='I agree to the Terms & Conditions',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1',activebackground='white', cursor='hand2', variable=check)
termsandconditions.grid(row=9, column=0, pady=10, padx=15)

signupButton = Button(frame,text='Sign up',font=('Microsoft Yeahei UI Light', 10, 'bold'),bd=0,bg='firebrick1',fg='white', activebackground='firebrick1',activeforeground='white',width=10,command=connect_database)
signupButton.grid(row=10,column=0,pady=10)

alreadyaccount = Label(frame, text='Dont have an acount?', font=('Open Sans','9' ,'bold'),bg='white', fg='firebrick1' )
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginButton = Button(frame, text='Log in', font=('Open Sans', 9,'bold underline'),bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',width=10,command=login_page)
loginButton.place(x=170,y=385)


signup_window.mainloop()