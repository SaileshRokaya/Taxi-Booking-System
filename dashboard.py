from tkinter import *
from tkinter.font import BOLD
from PIL import Image, ImageTk  # pip install pillow
import time
import databaseConnection
from tkinter import messagebox
import functools
from employeeDetails import employeeClass
from customerDetails import customerDetailsClass
from driverDetails import driverDetailsClass
from assignDriver import assignDriverClass
# from bookTrip import bookTripClass
from Welcompage import TBS
from payment import paymentClass



#======================================================================GUI_Designing======================================================================================
class DashboardClass:
    def __init__(self, root, email):
        self.root=root
        self.email=email
        self.root.geometry("1920x1080+0+0")
        self.root.state('zoomed')
        self.root.title("TBS-Taxi Booking System || Developed By Sailesh Rokaya")
        self.root.config(bg="white")

        #===========Title=============
        self.icon_title=PhotoImage(file="images/logo.png")
        title = Label(self.root, text="Taxi Booking System", image=self.icon_title,compound=LEFT, font=("time new roman", 40, "bold"),bg="#010c48",fg="white", anchor="w",padx=20).place(x=0,y=0, relwidth=1, height=70)

        #===========ProjectIcon=============
        photo = PhotoImage(file = "images/logo.png")
        self.root.iconphoto(False, photo)
        
        #============btn_logout=========
        btn_logout=Button(self.root, text="LogOut",  font=("elephant", 15, "bold"), bg="#010c48",fg="red",activeforeground="red", activebackground="#010c48",bd=0, cursor="hand2").place(x=1350,y=10, height=50, width=150)

        #============Clock===============
        self.lbl_clock = Label(self.root, text="Welcome to Taxi Booking System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS\t\t Welcome: "+email,font=("time new roman", 15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70, relwidth=1, height=30)

        #=============Left_Menu===========
        self.MenuLogo=Image.open("images/taxibookingsystm.png")
        self.MenuLogo=self.MenuLogo.resize((280,280), Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root, bd=2,relief=RIDGE, bg="white")
        LeftMenu.place(x=0,y=102,width=300,height=685)

        lbl_menuLogo=Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        #============lbl_Menu==================
        lbl_menu=Label(LeftMenu, text="Menu", font=("time new roman",20), bg="#009688").pack(side=TOP,fill=X)

        #============btn_Menu_List=============
        self.icon_side=PhotoImage(file="images/customer.png")
        btn_customer=Button(LeftMenu, text=" Customer", command=self.customerdetails, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("time new roman",20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        self.imgsupplier=PhotoImage(file="images/driver.png")
        btn_driver=Button(LeftMenu, text=" Taxi Driver", command=self.driverdetails, image=self.imgsupplier, compound=LEFT, padx=5, anchor="w", font=("time new roman",20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        self.imgcategory=PhotoImage(file="images/taxitrip.png")
        btn_assigndriv=Button(LeftMenu, text=" Assign Driver", command=self.assigndriver,  image=self.imgcategory, compound=LEFT, padx=5, anchor="w", font=("time new roman",20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        self.imgproduct=PhotoImage(file="images/employee.png")
        btn_employee=Button(LeftMenu, text=" Employee", command=self.employee, image=self.imgproduct, compound=LEFT, padx=5, anchor="w", font=("time new roman",20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        self.imgsales=PhotoImage(file="images/payment.png")
        btn_sales=Button(LeftMenu, text=" Payment", command=self.paymentFunc, image=self.imgsales, compound=LEFT, padx=5, anchor="w", font=("time new roman",20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        self.imgexit=PhotoImage(file="images/exit.png")      
        btn_exit=Button(LeftMenu, text=" Exit",command=quit, image=self.imgexit, compound=LEFT, padx=5, anchor="w", font=("time new roman",20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,fill=X)

        #============Content===================
        self.lbl_customer=Label(self.root, text="Total Customer\n[ 0 ]",bd=5,relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old sytyle", 20, "bold"))
        self.lbl_customer.place(x=350, y=120,height=150,width=250)

        self.lbl_employee=Label(self.root, text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE, bg="#009688", fg="white", font=("goudy old sytyle", 20, "bold"))
        self.lbl_employee.place(x=650, y=120,height=150,width=250)

        self.lbl_driver=Label(self.root, text="Total Taxi Driver\n[ 0 ]",bd=5,relief=RIDGE, bg="#607d8b", fg="white", font=("goudy old sytyle", 20, "bold"))
        self.lbl_driver.place(x=950, y=120,height=150,width=250)

        self.lbl_AvDriver=Label(self.root, text="Total Available \nDriver\n[ 0 ]",bd=5,relief=RIDGE, bg="#7F7F7F", fg="white", font=("goudy old sytyle", 20, "bold"))
        self.lbl_AvDriver.place(x=1250, y=120,height=150,width=250)

        self.lbl_UnAvDriver=Label(self.root, text="Total Unavailable \nDriver\n[ 0 ]",bd=5,relief=RIDGE, bg="#C42F11", fg="white", font=("goudy old sytyle", 20, "bold"))
        self.lbl_UnAvDriver.place(x=350, y=300,height=150,width=250)

        self.lbl_total_trip=Label(self.root, text="Total Booked \nTrip\n[ 0 ]",bd=5,relief=RIDGE, bg="#ffc107", fg="white", font=("goudy old sytyle", 20, "bold"))
        self.lbl_total_trip.place(x=650, y=300,height=150,width=250)

        self.lbl_conf_trip=Label(self.root, text="Total Confirmed \nTrip\n[ 0 ]",bd=5,relief=RIDGE, bg="#2E4CC5", fg="white", font=("goudy old sytyle", 20, "bold"))
        self.lbl_conf_trip.place(x=950, y=300,height=150,width=250)

        self.lbl_Unconf_trip=Label(self.root, text="Total \nUnconfirmed Trip\n[ 0 ]",bd=5,relief=RIDGE, bg="#410F05", fg="white", font=("goudy old sytyle", 20, "bold"))
        self.lbl_Unconf_trip.place(x=1250, y=300,height=150,width=250)

        self.lbl_can_trip=Label(self.root, text="Total Canceled \n Trip\n[ 0 ]",bd=5,relief=RIDGE, bg="#ff5722", fg="white", font=("goudy old sytyle", 20, "bold"))
        self.lbl_can_trip.place(x=350, y=480,height=150,width=250)

        self.lbl_closeBook=Label(self.root, text="Total Completed Trip\n[ 0 ]",bd=5,relief=RIDGE, bg="#865A68", fg="white", font=("goudy old sytyle", 20, "bold"))
        self.lbl_closeBook.place(x=650, y=480,height=150,width=250)

        self.lbl_income=Label(self.root, text="Total Revenu\n[ 0 ]",bd=5,relief=RIDGE, bg="#1CA345", fg="white", font=("goudy old sytyle", 20, "bold"))
        self.lbl_income.place(x=950, y=480,height=150,width=250)

        #============Footer====================
        lbl_footer = Label(self.root, text="TBS-Taxi Booking System || Developed By Sailesh Rokaya\n For Technical Support Student ID: 2020426 ",font=("time new roman", 15),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        self.update_date_time()
        self.updateContent()
#===================================================================================================

    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Taxi Booking System\t\t Date:{str(date_)} \t\t Time:{str(time_)} \t\t Welcome: "+self.email )
        self.lbl_clock.after(200,self.update_date_time) 

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
    
    def customerdetails(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=customerDetailsClass(self.new_win)

    def driverdetails(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=driverDetailsClass(self.new_win)

    def assigndriver(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=assignDriverClass(self.new_win)
    
    def paymentFunc(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=paymentClass(self.new_win)

    def LogOutFunc(self):
        self.withdraw=Toplevel(self.root)
        self.new_obj=TBS(self.withdraw) 
        self.root.destroy()

        

    def updateContent(self):
        databaseConnection
        try:
            databaseConnection.cur.execute("select * from customer where userType = 'Customer'")
            customer=databaseConnection.cur.fetchall()
            self.lbl_customer.config(text=f"Total Customer\n[ {str(len(customer))} ]")
            self.lbl_customer.after(10,self.updateContent) 

            databaseConnection.cur.execute("select * from registration where userType = 'Driver'")
            driver=databaseConnection.cur.fetchall()
            self.lbl_driver.config(text=f"Total Taxi \nDriver\n[ {str(len(driver))} ]")

            databaseConnection.cur.execute("select * from registration where userType = 'Driver' and status='Available'")
            Avdriver=databaseConnection.cur.fetchall()
            self.lbl_AvDriver.config(text=f"Total Available \nDriver\n[ {str(len(Avdriver))} ]")

            databaseConnection.cur.execute("select * from registration where userType = 'Driver' and status='Unavailable'")
            UnAvdriver=databaseConnection.cur.fetchall()
            self.lbl_UnAvDriver.config(text=f"Total Unavailable \nDriver\n[ {str(len(UnAvdriver))} ]")

            databaseConnection.cur.execute("select * from registration where userType = 'Employee'")
            employee=databaseConnection.cur.fetchall()
            self.lbl_employee.config(text=f"Total Employee\n[ {str(len(employee))} ]")

            databaseConnection.cur.execute("select * from booking")
            booking=databaseConnection.cur.fetchall()
            self.lbl_total_trip.config(text=f"Total Booked \nTrip\n[ {str(len(booking))} ]")

            databaseConnection.cur.execute("SELECT * from booking WHERE status='Conformed'")
            Confbooking=databaseConnection.cur.fetchall()
            self.lbl_conf_trip.config(text=f"Total Confirmed \nTrip\n[ {str(len(Confbooking))} ]")

            databaseConnection.cur.execute("SELECT * from booking WHERE status='Pending' ")
            UnConfbooking=databaseConnection.cur.fetchall()
            self.lbl_Unconf_trip.config(text=f"Total \nUnconfirmed Trip\n[ {str(len(UnConfbooking))} ]")

            databaseConnection.cur.execute("select * from booking where status='Canceled' and cancel='Yes'")
            Canbooking=databaseConnection.cur.fetchall()
            self.lbl_can_trip.config(text=f"Total Canceled \nTrip\n[ {str(len(Canbooking))} ]")

            databaseConnection.cur.execute("SELECT * FROM booking where status= 'Closed' or status= 'Paid'")
            CltTrip=databaseConnection.cur.fetchall()
            self.lbl_closeBook.config(text=f"Total Completed \nTrip\n[ {str(len(CltTrip))} ]")

            databaseConnection.cur.execute("SELECT SUM(grandTotal) FROM receipt ")
            Revenu=databaseConnection.cur.fetchone()
            # Convert Tuple to integer Using reduce() + lambda
            Rev = functools.reduce(lambda sub, ele: sub * 10 + ele, Revenu)
            self.lbl_income.config(text=f"Total Revenu \n [{(Rev)}] ")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

if __name__=="__main__":
    root = root=Tk()
    obj=DashboardClass(root)
    root.mainloop()
