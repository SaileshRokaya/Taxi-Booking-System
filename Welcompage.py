from tkinter import *
from tkinter.font import BOLD
from PIL import ImageTk  # pip install pillow
import time
from tkinter import messagebox
from tkinter import ttk
import functools
import databaseConnection
from dashboard import *
from customerRegistration import customerRegClass
from driverDashboard import DriverDashboardClass
from bookTrip import *
from forgotPassword import forgotPasswordClass



#======================================================================GUI_Designing======================================================================================
class TBS:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("1920x1080+0+0")
        self.root.state('zoomed')
        self.root.title("TBS-Taxi Booking System || Developed By Sailesh Rokaya")
        self.root.config(bg="#2E4CC5")

        # ===========================All Variables===========
        # self.var_email=StringVar()
        self.var_password=StringVar()
        self.var_utype=StringVar()
        # var_email=StringVar()
        self.var_email = StringVar()
        
        
        
        
        #===========Title=============
        self.icon_title=PhotoImage(file="images/logo.png")
        title = Label(self.root, text="Taxi Booking System", image=self.icon_title,compound=LEFT, font=("time new roman", 40, "bold"),bg="#010c48",fg="white", anchor="w",padx=20).place(x=0,y=0, relwidth=1, height=70)

        #===========ProjectIcon=============
        photo = PhotoImage(file = "images/logo.png")
        self.root.iconphoto(False, photo)
        
        #============Clock===============
        self.lbl_clock = Label(self.root,text="Welcome to Taxi Booking System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS" ,font=("time new roman", 15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70, relwidth=1, height=30)

        #=============LoginFrame===========
        Frame_Login=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        Frame_Login.place(x=1210, y=110, width=315, height=640)

        #===============ComboBoxForGender-Row-1==============================
        txt_Utype=ttk.Combobox(Frame_Login,textvariable=self.var_utype, values=("Select UserType","Customer","Driver","Employee"),state='readonly',justify=CENTER,font=("Andalus",10))
        txt_Utype.place(x=65,y=100, width=200, height=30)
        txt_Utype.current(0)

        #===============Label==============
        loginTitel=Label(Frame_Login,text="Login System", font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)
        lbl_email=Label(Frame_Login,text="Email*",bg="white", font=("Andalus",15), fg="#767171").place(x=0,y=150, relwidth=1)
        lbl_password=Label(Frame_Login,text="Password*", bg="white", font=("Andalus",15), fg="#767171").place(x=0,y=230,relwidth=1)
        lbl_hr=Label(Frame_Login, bg="lightgray").place(x=38,y=490,width=250,height=2)

        lbl_hrOR=Label(Frame_Login,text="OR", bg="white",font=("times new roman",15,"bold")).place(x=150,y=475)
        lbl_member=Label(Frame_Login,text="Don't have an account?", bg="white",font=("times new roman",10)).place(x=80,y=535)
        #===============TextBox==============
        txtemail=Entry(Frame_Login, textvariable=self.var_email, font=("Andalus",10),bg="white", fg="#767171").place(x=65,y=190, width=200, height=30)
        txtpassword=Entry(Frame_Login, textvariable=self.var_password, font=("Andalus",10), bg="white", show="*", fg="#767171").place(x=65,y=280, width=200, height=30)
        #============btn_logout=========
        btn_logIn=Button(Frame_Login, text="LogIn",command=self.LogIn, font=("time new roman", 15, "bold"), bg="#418BCA",activebackground="#418BCA", cursor="hand2").place(x=65,y=350, height=35, width=200)
        btn_cancel=Button(Frame_Login, text="Cancel",command=quit, font=("time new roman", 15, "bold"), bg="#C42F11",activebackground="#C42F11", cursor="hand2").place(x=65,y=420, height=35, width=200)
        btn_forgot=Button(Frame_Login, text="Forgot Password?", command=self.forgotPassword, font=("time new roman", 10),bd=0, bg="white",activebackground="white",fg="#418BCA",activeforeground="#418BCA", cursor="hand2").place(x=95,y=500, height=35, width=150)
        btn_Signup=Button(Frame_Login, text="Sign Up", command=self.reg, font=("time new roman", 10),bd=0, bg="white",activebackground="white",fg="#418BCA",activeforeground="#418BCA", cursor="hand2").place(x=210,y=529, height=35, width=60)


        #============images=====================
        self.image1=PhotoImage(file="images/slid1.png")
        self.image2=ImageTk.PhotoImage(file="images/slid3.jpg")

        #=============SilderFrame=============
        Frame_slider=Frame(self.root)
        Frame_slider.place(x=0,y=100,width=1200,height=700)

        self.lblimg1=Label(Frame_slider,image=self.image1,bd=0)
        self.lblimg1.place(x=0,y=0)

        self.lblimg2=Label(Frame_slider,image=self.image2,bd=0)
        self.lblimg2.place(x=1100,y=0)
        self.x=1100
        self.slider_func()

        #============Footer====================
        lbl_footer = Label(self.root, text="TBS-Taxi Booking System || Developed By Sailesh Rokaya\n For Technical Support Student ID: 2020426 ",font=("time new roman", 15),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        self.update_date_time()
         
    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Taxi Booking System\t\t Date:{str(date_)} \t\t Time:{str(time_)} ")
        self.lbl_clock.after(200,self.update_date_time)
        
        

    def DashboardFunc(self, email):
        # self.root.destroy()
        self.new_win=Toplevel(self.root)
        self.new_obj=DashboardClass(self.new_win, email) 
        self.root.withdraw()

    def BookingFunc(self,email):
        # email=self.var_email.get()
        self.new_win=Toplevel(self.root)
        self.new_obj=bookTripClass(self.new_win, email)
    
    def driverDahsboard(self,email):
        self.new_win=Toplevel(self.root)
        self.new_obj=DriverDashboardClass(self.new_win, email)

    def forgotPassword(self):
        # self.root.destroy()
        self.new_win=Toplevel(self.root)
        self.new_obj=forgotPasswordClass(self.new_win) 


    def slider_func(self):
        self.x-=1
        if self.x==0:
            self.x=1100
            time.sleep(1)

            #====swap====
            self.newimg=self.image1
            self.image1=self.image2
            self.image2=self.newimg

            self.lblimg1.config(image=self.image1)
            self.lblimg2.config(image=self.image2)
        self.lblimg2.place(x=self.x,y=0)
        self.lblimg2.after(1,self.slider_func)

#=============Functions=============

    def reg(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=customerRegClass(self.new_win)
        
    #=====================================DatabaseConnectionForLogin====================================
    # def getemail(self):
    #     var_email.get()
    def LogIn(self):
        email = self.var_email.get()
        password = self.var_password.get()
        # Establish Connection
        databaseConnection
        # Find user If there is any take proper action
        try:
            if self.var_utype.get()=="Select UserType":
                messagebox.showwarning("Error","User Type must be requird!")
            elif self.var_utype.get()=="Employee":
                find_emp = ('SELECT * FROM registration WHERE email = ? and password = ? and userType = "Employee"')
                databaseConnection.cur.execute(find_emp, [email, password])
                resultEmp = databaseConnection.cur.fetchall()
            elif self.var_utype.get()=="Driver":
                find_driver = ('SELECT * FROM registration WHERE email = ? and password = ? and userType = "Driver"')
                databaseConnection.cur.execute(find_driver, [email, password])
                resultDriv = databaseConnection.cur.fetchall()
            elif self.var_utype.get()=="Customer":
                find_cus = ('SELECT * FROM customer WHERE email = ? and password = ?')
                databaseConnection.cur.execute(find_cus, [email, password])
                resultCus = databaseConnection.cur.fetchall()
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)
 
        try:
            if self.var_email.get() == "" or self.var_password.get()=="":
                messagebox.showerror("Error", "Email,Password Must be required", parent=self.root)
            
            elif self.var_utype.get()=="Employee" and resultEmp:
                print(email, "user logged in")
                messagebox.showinfo("Success", "Login Successfully")
                self.var_utype.set("Select UserType")
                # self.var_email.set("")
                self.var_password.set("")
                self.DashboardFunc(email)
            
            elif self.var_utype.get()=="Driver" and resultDriv:
                print(email, "user logged in")
                messagebox.showinfo("Success", "Login Successfully")
                self.var_utype.set("Select UserType")
                # self.var_email.set("")
                self.var_password.set("")
                self.driverDahsboard(email)
                
            
            elif self.var_utype.get()=="Customer" and resultCus:
                # print(email, "user logged in")
                messagebox.showinfo("Success", "Login Successfully")
                self.var_utype.set("Select UserType")
                # self.var_email.set("")
                self.var_password.set("")
                self.BookingFunc(email)

            else:
                messagebox.showerror("Error", "Invalid email and password")

        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)


  



if __name__=="__main__":
    obj=TBS()
    mainloop()
