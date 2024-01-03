from tkinter import * 
from tkinter import messagebox
import tkinter as tk
import ast
import pymysql
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
import re
import webbrowser
import time


root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def style_window(window):
    window.configure(bg="#57a1f8")  # Change the background color

    # Apply styling to buttons
    for widget in window.winfo_children():
        if isinstance(widget, Button):
            widget.configure(
                bg='#fff', fg='#57a1f8', font=('Microsoft YaHei UI Light', 14, 'bold'), pady=10, cursor='hand2'
            )


def signin():
    username = user.get()
    password = code.get()

    if username == '' or password=='':
        messagebox.showerror('Error','All Fields Are Required')

    else:        
        try:
            con=pymysql.connect(host='localhost',user='root',password='1234')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error',"Database connection not established")
            return

        query = 'use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(username,password))
        row=mycursor.fetchone()

        if row == None:
            messagebox.showerror('Invalid',"Invalid Username and Password")
        
        else:
            #messagebox.showinfo('Welcome', " Login Successful")
            root.withdraw()
            screen= Toplevel(root)
            screen.title("App")
            screen.geometry('925x500+300+200')
            screen.resizable(False,False)
            style_window(screen)

            def moisture():
                
                mscreen= Toplevel(root)
                mscreen.title("Moisture")
                mscreen.geometry('925x500+300+200')
                mscreen.config(bg="white")

                days = np.arange(1, 11)
                soil_moisture = np.array([30, 35, 42, 38, 48, 50, 55, 62, 67, 72])
                start_date = datetime(2023, 9, 1)
                date_list = [start_date + timedelta(days=int(day) - 1) for day in days]

                frame = Frame(mscreen)
                frame.pack(expand=True, fill='both')

                fig, ax = plt.subplots(figsize=(10, 6))
                ax.plot(date_list, soil_moisture, marker='o', linestyle='-', color='b', label='Soil Moisture')
                ax.set_title('Soil Moisture Over Time - September 2023')
                ax.set_xlabel('Date')
                ax.set_ylabel('Soil Moisture (%)')
                ax.grid(True, linestyle='--', alpha=0.7)
                ax.legend()
                plt.xticks(rotation=45, ha='right')

                canvas = FigureCanvasTkAgg(fig, master=frame)
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.pack(expand=True, fill='both')

                mscreen.mainloop()
                           


            def temp():

                tscreen = Toplevel(root)
                tscreen.title("Temperature")
                tscreen.geometry('925x500+300+200')
                tscreen.config(bg="white")


                days = np.arange(1, 11)
                high_temps = np.array([25, 28, 30, 32, 28, 26, 24, 22, 23, 25])
                low_temps = np.array([15, 18, 20, 22, 18, 16, 14, 12, 13, 15])
                start_date = datetime(2023, 9, 1)
                date_list = [start_date + timedelta(days=int(day) - 1) for day in days]
                
                frame = Frame(tscreen)
                frame.pack(expand=True,fill='both')

                fig, ax = plt.subplots(figsize=(10, 6))
                ax.plot(date_list, high_temps, marker='o', linestyle='-', color='r', label='High Temp')
                ax.plot(date_list, low_temps, marker='o', linestyle='-', color='b', label='Low Temp')
                ax.set_title('Daily Temperature in Farming Area - September 2023')
                ax.set_xlabel('Date')
                ax.set_ylabel('Temperature (°C)')
                ax.grid(True, linestyle='--', alpha=0.7)
                ax.legend()
                plt.xticks(rotation=45, ha='right')

                canvas = FigureCanvasTkAgg(fig, master=frame)
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.pack(expand=True, fill='both')

                tscreen.mainloop()


            def motion():
                motion_screen = Toplevel(root)
                motion_screen.title("Temperature")
                motion_screen.geometry('925x500+300+200')
                motion_screen.config(bg="white")

                days = np.arange(1, 11)
                motion_data = np.array([0, 1, 0, 1, 0, 0, 1, 1, 0, 1])
                start_date = datetime(2023, 9, 1)
                date_list = [start_date + timedelta(days=int(day) - 1) for day in days]

                frame = Frame(motion_screen)
                frame.pack(expand=True,fill='both')

                fig, ax = plt.subplots(figsize=(10, 6))
                ax.step(date_list, motion_data, where='post', color='g', label='Motion Detection')
                ax.set_title('Motion Detection Over Time - September 2023')
                ax.set_xlabel('Date')
                ax.set_ylabel('Motion Detected (1) / No Motion Detected (0)')
                ax.grid(True, linestyle='--', alpha=0.7)
                ax.legend()
                plt.xticks(rotation=45, ha='right')

                canvas = FigureCanvasTkAgg(fig, master=frame)
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.pack(expand=True, fill='both')

                motion_screen.mainloop()

            def feed():
                link = "https://forms.gle/udnRJnSN1EEThssf9"
                webbrowser.open_new(link)
            
            def motor_ON():
                if button.cget("text") == "Motor ON":
                    button.config(text='Motor OFF' , bg='red')
                else:
                    button.config(text='Motor ON' , bg='#1fd655')
                

            def clear():
                user.delete(0,END)

            def logout():
                #clear()
                screen.destroy()
                root.wm_deiconify()

            #Label(screen,text=f'Smart Agriculture, Welcome {username}',bg='#fff',font=('Calibri(Body)',30,'bold')).pack(expand=True)
            img = PhotoImage(file='signup.png')
            Label(screen,image=img,border=0,bg='white').place(x=50,y=90)

            frame = Frame(screen,width=400,height=420,bg='#fff')
            frame.place(x=500,y=20)

            heading = Label(frame,text=f"Welcome {username}",fg="#57a1f8",bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
            heading.place(x=60,y=40)
            Button(frame, width=39,pady=7,text='Soil Moisture',bg='#57a1f8',cursor='hand2',fg='white',border=0,command=moisture).place(x=60,y=140)
            Button(frame, width=39,pady=7,text='Temperature',bg='#57a1f8',cursor='hand2',fg='white',border=0,command=temp).place(x=60,y=200)
            Button(frame, width=39,pady=7,text='Motion',bg='#57a1f8',cursor='hand2',fg='white',border=0,command=motion).place(x=60,y=260)
            button = tk.Button(frame, width=39,pady=7,text='Motor ON',bg='#1fd655',cursor='hand2',fg='white',border=0,command=motor_ON)
            button.place(x=60,y=320)
            Button(frame, width=8,text='(Log Out)',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=logout).place(x=100,y=380)
            Button(frame, width=8,text='(Feedback)',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=feed).place(x=250,y=380)
            screen.mainloop()

# SIGN UP PAGE

def signup_command():
    root.withdraw()
    window = Toplevel(root)
    window.title("SignUp")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False,False)
    style_window(window)



    def signup():
        
        fullname = Fname.get()
        email    = mail.get()
        phone_number = phone.get()
        username = user.get()
        password = code.get()
        confirm_password = confirm_code.get()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        def clear():
            Fname.delete(0,END)
            mail.delete(0,END)
            user.delete(0,END)
            code.delete(0,END)
            confirm_code.delete(0,END)

        def  valid_email(mail):
            pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
            if re.match(pattern,mail):
                return True
            else:
                return False

        def valid_no(phone):
            pattern = re.compile(r'^[6789]\d{9}$')
            if re.match(pattern,phone):
                return True
            else:
                return False
        def strong_passwrod(pswrd):
            if len(password) < 6:
                 return False
            if not any(char.isupper() for char in password):
                return False
            if not any(char.islower() for char in password):
                return False
            if not any(char.isdigit() for char in password):
                return False
            if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
                return False
            return True

            
        if fullname=='Full Name' or email=='Email' or phone_number=='Phone Number' or username == 'Username' or password=='Password' or confirm_password=='Confirm Password':
            messagebox.showerror('Invalid','All fields Are Required')

        elif valid_email(email) == False:
            messagebox.showerror('Invali','Enter a Valid Email-ID')
        
        elif valid_no(phone_number)== False:
            messagebox.showerror('Invalid','Enter a non-zero starting 10 digit number') 
        
        elif strong_passwrod(password) == False:
            messagebox.showerror('ERROR',"Please enter a strong password of atleast contain 6 character including uppercase, lowercase, number and special character")
        
        elif password!=confirm_password:
            messagebox.showerror('Invalid','Both the passwords does not match!')

        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='1234')
                mycursor=con.cursor()
            except:
                messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
                return
            
            try:
                query = 'create database userdata'
                mycursor.execute(query)
                query='use userdata'
                mycursor.execute(query)
                query = 'create table data(id int auto_increment primary key not null,Fullname varchar(100),Email varchar(100),PhoneNumber varchar(100), username varchar(100), password varchar(20), TimeStamp varchar(20))'
                mycursor.execute(query)
            
            except:
                mycursor.execute('use userdata')
            query = 'select * from data where username=%s'
            mycursor.execute(query,(username))

            row = mycursor.fetchone()
            if row!=None:
                messagebox.showerror("Error",'Username Already Exist, Please use a different username')
            
            else:
                query = 'insert into data(Fullname, Email, PhoneNumber, username,password, TimeStamp) values(%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(fullname, email, phone_number, username, password, timestamp))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Sign Up Successfull')

                clear()
                window.destroy()
                root.wm_deiconify()


    def sign():
        window.destroy()
        root.wm_deiconify()    
        
    img = PhotoImage(file='farmer.png')    
    Label(window,image=img,border=0,bg='white').place(x=0,y=0)

    frame = Frame(window,width=350,height=600,bg='#fff')
    frame.place(x=480,y=0)

    heading = Label(frame,text="Sign Up",fg="#57a1f8",bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=100,y=10)

    # Full Name
    def on_enter(e):
        Fname.delete(0, 'end')
    def on_leave(e):
        if Fname.get()=='':
            Fname.insert(0,"Full Name")


    Fname = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    Fname.place(x=30,y=70)
    Fname.insert(0, 'Full Name')
    Fname.bind("<FocusIn>", on_enter)
    Fname.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=97)

    # Last Name
    def on_enter(e):
        mail.delete(0, 'end')
    def on_leave(e):
        if mail.get()=='':
            mail.insert(0,"Email")


    mail = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    mail.place(x=30,y=120)
    mail.insert(0, 'Email')
    mail.bind("<FocusIn>", on_enter)
    mail.bind("<FocusOut>", on_leave)                                                                                  

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=147)

    # Phone Number
    def on_enter(e):
        phone.delete(0, 'end')
    def on_leave(e):
        if phone.get()=='':
            phone.insert(0,"Phone Number")


    phone = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    phone.place(x=30,y=170)
    phone.insert(0, 'Phone Number')
    phone.bind("<FocusIn>", on_enter)
    phone.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=197)

    # Username
    def on_enter(e):
        user.delete(0, 'end')
    def on_leave(e):
        if user.get()=='':
            user.insert(0,"Username")


    user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    user.place(x=30,y=220)
    user.insert(0, 'Username')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)


    # Password
    def on_enter(e):
        code.delete(0, 'end')
    def on_leave(e):
        if code.get()=='':
            code.insert(0,"Password")


    code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    code.place(x=30,y=270)
    code.insert(0, 'Password')
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=297)

    # Confirm Password
    def on_enter(e):
        confirm_code.delete(0, 'end')
    def on_leave(e):
        if confirm_code.get()=='':
            confirm_code.insert(0,"Confirm Password")


    confirm_code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    confirm_code.place(x=30,y=320)
    confirm_code.insert(0, 'Confrim Password')
    confirm_code.bind("<FocusIn>", on_enter)
    confirm_code.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=347)


    # Sign Up Button 

    Button(frame, width=39,pady=7,text='Sign Up',bg='#57a1f8',cursor='hand2',fg='white',border=0, command=signup).place(x=35,y=370)
    label = Label(frame, text='Already have an account?',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label.place(x=55,y=410)

    signin = Button(frame, width=6,text='Sign In',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign)
    signin.place(x=200,y=410)

    window.mainloop()

# LOGIN PAGE
img = PhotoImage(file='farmer.png')
# resized_img = img.subsample(500,500)
Label(root,image=img,bg='green',).place(x=0,y=0)

frame = Frame(root,width=350,height=350,bg="white")
frame.pack(expand='True',fill='both')
frame.place(x=480,y=70)

# Heading

heading=Label(frame, text='Sign In', fg='#57a1f8',bg='white',font=('Microsoft yaHei UI Light',23,'bold'))
heading.place(x=100,y=10)

# username

def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0,"Username")
    

user = Entry(frame,width=25,fg='black',border=0,bg="white",font=("Microsoft YaHei UI Light",11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

# password

def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0,"Password")



code = Entry(frame,width=25,fg='black',border=0,bg="white",font=("Microsoft YaHei UI Light",11),show='*')
code.place(x=30,y=150)
code.insert(0,'Password')
#code = Entry(frame,width=25,fg='black',border=0,bg="white",font=("Microsoft YaHei UI Light",11),show='*')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)



Button(frame,width=39,pady=7,text='Sign In',bg='#57a1f8',fg='white',border=0,command=signin,cursor='hand2').place(x=35,y=204)
label = Label(frame, text="Don't have an account?", fg='black',bg='white',font=("Microsoft YaHei UI Light",9))
label.place(x=75,y=270)

sign_up = Button(frame,width=6,text='Sign Up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup_command)
sign_up.place(x=215,y=270)

style_window(root)

root.mainloop()
