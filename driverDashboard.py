from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk
from tkinter import messagebox
import functools
import databaseConnection



#======================================================================GUI_Designing======================================================================================
class DriverDashboardClass:
    def __init__(self, root, email):
        self.root=root
        self.email=email
        self.root.geometry("1100x500+10+130")
        self.root.title("Assign Driver || TBS-Taxi Booking System || Developed By Sailesh Rokaya")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(0,0)
        self.Table()

        
        #===========ProjectIcon=============
        photo = PhotoImage(file = "images/taxitrip.png")
        self.root.iconphoto(False, photo)

        #================titel====================================
        title=Label(self.root, text="Driver Dashboard", font=("goudy old style",20,"bold"),bg="#0f4d7d", fg="white").place(x=30,y=15, width=1040)

        
        
        #===============BookedFrame=========================
        foot=LabelFrame(self.root,  font=("goudy old style",12,"bold"), bd=2, relief=RIDGE, bg="white")
        foot.place(x=30, y=380, width=1040, height=100)
        lbl_tl=Label(foot, text="Note: Mr. " + self.email +"  After complete trip please hit the 'Complete Trip' button to update your status.", font=("goudy old style",15),bg="white").place(x=10,y=35)
        #==========================UpdateStatusBtn==============================
        btn_Cstatus=Button(foot,text="Complete Trip", command=self.ChangeStatus,  font=("goudy old style",15), bg="#4caf50", activebackground="#4caf50", fg="white", activeforeground="white",cursor="hand2").place(x=890,y=35,width=125,height=30)
        
    def Table(self):
        #===============BookedFrame=========================
        NewBook=LabelFrame(self.root,  font=("goudy old style",12,"bold"), bd=2, relief=RIDGE, bg="white")
        NewBook.place(x=30, y=70, width=500, height=300)
        #================BookedTitel====================================
        Bookedtitle=Label(NewBook, text="Your New Trip List", font=("goudy old style",15,"bold"),bg="#418BCA", fg="white").pack(side=TOP,fill=X)
        #=================Scrollbar=============================
        scrolly=Scrollbar(NewBook,orient=VERTICAL)
        scrollx=Scrollbar(NewBook,orient=HORIZONTAL)
        #=================BookedTripTable=============================                                               
        self.RegistrationTable=ttk.Treeview(NewBook,columns=("booking.booking_id","booking.picDate","booking.dropDate","booking.picTime","booking.dropTime","booking.picAddress","booking.dropAddress","booking.status","registration.name","customer.name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)                       #b.booking_id, b.picDate, b.dropDate, b.picTime, b.dropTime, b.picAddress, b.dropAddress, r.name,c.name
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.RegistrationTable.xview)
        scrolly.config(command=self.RegistrationTable.yview)
        
        self.RegistrationTable.heading("booking.booking_id",text="Booking ID")
        self.RegistrationTable.heading("booking.picDate",text="Pick-Up Date")
        self.RegistrationTable.heading("booking.dropDate",text="Drop Date")
        self.RegistrationTable.heading("booking.picTime",text="Pick-Up Time")
        self.RegistrationTable.heading("booking.dropTime",text="Drop Time")
        self.RegistrationTable.heading("booking.picAddress",text="Pick-Up Address")
        self.RegistrationTable.heading("booking.dropAddress",text="Drop Address")
        self.RegistrationTable.heading("booking.status",text="Status")
        self.RegistrationTable.heading("registration.name",text="Driver")
        self.RegistrationTable.heading("customer.name",text="Customer")
      
        
        self.RegistrationTable["show"]="headings"
        self.RegistrationTable.column("booking.booking_id",width=80)
        self.RegistrationTable.column("booking.picDate",width=100)
        self.RegistrationTable.column("booking.dropDate",width=100)
        self.RegistrationTable.column("booking.picTime",width=100)
        self.RegistrationTable.column("booking.dropTime",width=100)
        self.RegistrationTable.column("booking.picAddress",width=100)
        self.RegistrationTable.column("booking.dropAddress",width=100)
        self.RegistrationTable.column("booking.status",width=100)
        self.RegistrationTable.column("registration.name",width=100)
        self.RegistrationTable.column("customer.name",width=100)
        
       
        self.RegistrationTable.pack(fill=BOTH,expand=1)
        # self.RegistrationTable.bind("<ButtonRelease-1>",self.get_Booked_data)
        self.showNewData()


        #===============BookedFrame=========================
        ClosedBook=LabelFrame(self.root,  font=("goudy old style",12,"bold"), bd=2, relief=RIDGE, bg="white")
        ClosedBook.place(x=570, y=70, width=500, height=300)
        #================BookedTitel====================================
        Closetitle=Label(ClosedBook, text="Your Old Trip List", font=("goudy old style",15,"bold"),bg="#C42F11", fg="white").pack(side=TOP,fill=X)
        #=================Scrollbar=============================
        scrolly=Scrollbar(ClosedBook,orient=VERTICAL)
        scrollx=Scrollbar(ClosedBook,orient=HORIZONTAL)
        #=================BookedTripTable=============================                                               
        self.RegistrationTable=ttk.Treeview(ClosedBook,columns=("booking.booking_id","booking.picDate","booking.dropDate","booking.picTime","booking.dropTime","booking.picAddress","booking.dropAddress","booking.status","registration.name","customer.name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)                       #b.booking_id, b.picDate, b.dropDate, b.picTime, b.dropTime, b.picAddress, b.dropAddress, r.name,c.name
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.RegistrationTable.xview)
        scrolly.config(command=self.RegistrationTable.yview)
        
        self.RegistrationTable.heading("booking.booking_id",text="Booking ID")
        self.RegistrationTable.heading("booking.picDate",text="Pick-Up Date")
        self.RegistrationTable.heading("booking.dropDate",text="Drop Date")
        self.RegistrationTable.heading("booking.picTime",text="Pick-Up Time")
        self.RegistrationTable.heading("booking.dropTime",text="Drop Time")
        self.RegistrationTable.heading("booking.picAddress",text="Pick-Up Address")
        self.RegistrationTable.heading("booking.dropAddress",text="Drop Address")
        self.RegistrationTable.heading("booking.status",text="Status")
        self.RegistrationTable.heading("registration.name",text="Driver")
        self.RegistrationTable.heading("customer.name",text="Customer")
        
      
        
        self.RegistrationTable["show"]="headings"
        self.RegistrationTable.column("booking.booking_id",width=80)
        self.RegistrationTable.column("booking.picDate",width=100)
        self.RegistrationTable.column("booking.dropDate",width=100)
        self.RegistrationTable.column("booking.picTime",width=100)
        self.RegistrationTable.column("booking.dropTime",width=100)
        self.RegistrationTable.column("booking.picAddress",width=100)
        self.RegistrationTable.column("booking.dropAddress",width=100)
        self.RegistrationTable.column("booking.status",width=100)
        self.RegistrationTable.column("registration.name",width=100)
        self.RegistrationTable.column("customer.name",width=100)
        
        
        
        
        self.RegistrationTable.pack(fill=BOTH,expand=1)
        # self.RegistrationTable.bind("<ButtonRelease-1>",self.get_Booked_data)
        self.showClosedData()

#    ======================================================DatabaseConnections=============================================================================
    # =====================ShowLoginDriver'sCustomerOnly======================
    def showNewData(self):
        databaseConnection
        # Find_User
        find_userId=("SELECT reg_id from registration WHERE email = '%s'" % (self.email))
        databaseConnection.cur.execute(find_userId)
        userId=databaseConnection.cur.fetchone()[0]
        print(userId)
        try:                              
            databaseConnection.cur.execute("select booking.booking_id, booking.picDate,booking.dropDate, booking.picTime, booking.dropTime, booking.picAddress, booking.dropAddress, booking.status, registration.name, customer.name from booking  LEFT OUTER JOIN registration  on registration.reg_id=booking.reg_id JOIN customer  on customer.c_id=booking.c_id WHERE booking.status='Conformed' and registration.reg_id=? ",(
                                userId,
                                ))
            rows = databaseConnection.cur.fetchmany()
            print(rows)
            self.RegistrationTable.delete(*self.RegistrationTable.get_children())
            for row in rows:
                self.RegistrationTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)


    # =====================ShowLoginDriver'sCustomerOnly======================
    def showClosedData(self):
        databaseConnection
        # Find_User
        find_userId=("SELECT reg_id from registration WHERE email = '%s'" % (self.email))
        databaseConnection.cur.execute(find_userId)
        userId=databaseConnection.cur.fetchone()[0]
        print(userId)
        try:                               #select b.booking_id, b.picDate, b.dropDate, b.picTime, b.dropTime, b.picAddress, b.dropAddress, r.name,c.name from booking b  JOIN registration r on r.reg_id=b.reg_id JOIN customer c on c.c_id=b.c_id where b.status='Active' and r.email= ? 
            databaseConnection.cur.execute("select booking.booking_id, booking.picDate,booking.dropDate, booking.picTime, booking.dropTime, booking.picAddress, booking.dropAddress, booking.status, registration.name, customer.name from booking  LEFT OUTER JOIN registration  on registration.reg_id=booking.reg_id JOIN customer  on customer.c_id=booking.c_id where (booking.status= 'Closed' or booking.status= 'Paid') and registration.reg_id= ? ",(
                                userId,
                                ))
            rows = databaseConnection.cur.fetchall()
            print(rows)
            self.RegistrationTable.delete(*self.RegistrationTable.get_children())
            for row in rows:
                self.RegistrationTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)

    #===============================ToChangeTheStatusOfDriverAndBooking===========================
    def ChangeStatus(self):
        databaseConnection
        # Find_User
        find_userId=("SELECT reg_id from registration WHERE email = '%s'" % (self.email))
        databaseConnection.cur.execute(find_userId)
        userId=databaseConnection.cur.fetchone()[0]
        try:                 
            databaseConnection.cur.execute("Update registration set status='Available' where reg_id=?",
                                    (userId,))
            databaseConnection.con.commit()
            self.ChangeBookingStatus()
            messagebox.showinfo("Status", "Status Successfully Update", parent=self.root)
            self.Table()
            
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)

    def ChangeBookingStatus(self):
        databaseConnection
        # Find_User
        find_userId=("SELECT reg_id from registration WHERE email = '%s'" % (self.email))
        databaseConnection.cur.execute(find_userId)
        userId=databaseConnection.cur.fetchone()[0]
        #  Find BookingId
        databaseConnection.cur.execute("SELECT booking_id FROM booking WHERE reg_id=? and status='Conformed'",(userId,))
        bookingId=databaseConnection.cur.fetchone()
        bookId = functools.reduce(lambda sub, ele: sub * 10 + ele, bookingId)
        try:                                
            databaseConnection.cur.execute("Update booking set status='Closed' where booking_id=?",
                   (bookId, ))
            databaseConnection.con.commit()

        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)


#==========MainMethod============           
if __name__=="__main__":
    root=Tk()
    obj=DriverDashboardClass(root)
    root.mainloop()