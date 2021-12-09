from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk
from tkinter import messagebox
import functools
import databaseConnection



#======================================================================GUI_Designing======================================================================================
class assignDriverClass:
    def __init__(self, root):
        # self.bookTripClass=bookTripClass
        self.root=root
        self.root.geometry("1100x500+300+130")
        self.root.title("Assign Driver || TBS-Taxi Booking System || Developed By Sailesh Rokaya")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(0,0)

        # ===========================All Variables===========

        self.cust_list=[]
        self.driv_list=[]
        self.var_customer=StringVar()
        self.var_driver=StringVar()
        self.var_bookingId=StringVar()
        self.ViewTable()
        self.fetch_driver_Name()
        
        #===========ProjectIcon=============
        photo = PhotoImage(file = "images/taxitrip.png")
        self.root.iconphoto(False, photo)

        #================titel====================================
        title=Label(self.root, text="Assign Driver", font=("goudy old style",20,"bold"),bg="#0f4d7d", fg="white").place(x=30,y=15, width=1040)

        #===============AssignFrame=========================
        frmAssign=LabelFrame(self.root,  font=("goudy old style",12,"bold"), bd=2, relief=RIDGE, bg="white")
        frmAssign.place(x=30, y=60, width=1040, height=100)
        #===============ComboBoxOptions=======================
        cmb_Customer=ttk.Combobox(frmAssign, textvariable=self.var_customer, values=self.cust_list,state='readonly',justify=CENTER,font=("goudy old style",10))
        cmb_Customer.place(x=130,y=35,width=200, height=30)
        
        cmb_driver=ttk.Combobox(frmAssign, textvariable=self.var_driver, values=self.driv_list,state='readonly',justify=CENTER,font=("goudy old style",10))
        cmb_driver.place(x=560,y=35,width=200, height=30)
        # cmb_driver.current(0)
        #================Label===============================
        lbl_Customer=Label(frmAssign, text="Customer",font=("goudy old style",15), bg="white").place(x=30,y=35)
        lbl_Driver=Label(frmAssign, text="Assign To Driver",font=("goudy old style",15), bg="white").place(x=400,y=35)
        
        #================Btn_Assign===============================
        btn_search=Button(frmAssign,text="Assigned", command=self.AssignDriver, font=("goudy old style",15), bg="#4caf50", activebackground="#4caf50", fg="white", activeforeground="white",cursor="hand2").place(x=810,y=35,width=150,height=30)
        self.ViewTable()
        self.fetch_driver_Name()

    def ViewTable(self):
        #===============BookedFrame=========================
        frmBooked=LabelFrame(self.root,  font=("goudy old style",12,"bold"), bd=2, relief=RIDGE, bg="white")
        frmBooked.place(x=30, y=170, width=510, height=300)
        #================BookedTitel====================================
        Bookedtitle=Label(frmBooked, text="Unconformed Trip List", font=("goudy old style",15,"bold"),bg="#ffc107", fg="white").pack(side=TOP,fill=X)
        #=================Scrollbar=============================
        scrolly=Scrollbar(frmBooked,orient=VERTICAL)
        scrollx=Scrollbar(frmBooked,orient=HORIZONTAL)
        #=================BookedTripTable=============================  booking.booking_id, booking.picDate, booking.picTime, booking.dropTime, booking.picAddress, booking.dropAddress, booking.status, registration.name, customer.name                                              
        self.RegistrationTable=ttk.Treeview(frmBooked,columns=("booking.booking_id","booking.picDate","booking.dropDate","booking.picTime","booking.dropTime","booking.picAddress","booking.dropAddress","booking.status","registration.name","customer.name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)                
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
        self.showUnconformed()
        
        #===============ConformedFrame=========================
        frmConform=LabelFrame(self.root,  font=("goudy old style",12,"bold"), bd=2, relief=RIDGE, bg="white")
        frmConform.place(x=560, y=170, width=510, height=300)
        #================ConformedTitel====================================
        Conformedtitle=Label(frmConform, text="Conformed Trip List", font=("goudy old style",15,"bold"),bg="#2E4CC5", fg="white").pack(side=TOP,fill=X)
        #=================Scrollbar=============================
        scrolly=Scrollbar(frmConform,orient=VERTICAL)
        scrollx=Scrollbar(frmConform,orient=HORIZONTAL)
        #=================ConformedTripTable=============================                                               
        self.RegistrationTable=ttk.Treeview(frmConform,columns=("booking.booking_id","booking.picDate","booking.dropDate","booking.picTime","booking.dropTime","booking.picAddress","booking.dropAddress","booking.status","registration.name","customer.name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
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
        self.showConformed()

    # =====================ShowBookedData======================
    def showUnconformed(self):
        databaseConnection
        try:                                #select b.booking_id, b.picDate, b.dropDate, b.picTime, b.dropTime, b.picAddress, b.dropAddress, r.name,c.name from booking b  JOIN registration r on r.reg_id=b.reg_id JOIN customer c on c.c_id=b.c_id
            databaseConnection.cur.execute("select booking.booking_id, booking.picDate,booking.dropDate, booking.picTime, booking.dropTime, booking.picAddress, booking.dropAddress, booking.status, registration.name, customer.name from booking  LEFT OUTER JOIN registration  on registration.reg_id=booking.reg_id JOIN customer  on customer.c_id=booking.c_id WHERE booking.status='Pending' and cancel='No'")
            rows = databaseConnection.cur.fetchall()  
            # print(rows)
            self.RegistrationTable.delete(*self.RegistrationTable.get_children())
            for row in rows:
                self.RegistrationTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)

    # def get_Booked_data(self, ev):
    #     f = self.RegistrationTable.focus()
    #     content = (self.RegistrationTable.item(f))
    #     row = content['values']
    #     self.var_driver.set(row[8]),
    #     self.var_customer.set(row[9]),
        

    #===================FetchDataInComboBox========
    def fetch_driver_Name(self):
        self.driv_list.append("Empty")
        self.cust_list.append("Empty")
        databaseConnection
        try:
            databaseConnection.cur.execute("select c.name from customer c INNER JOIN booking b on c.c_id=b.c_id WHERE status='Pending' and reg_id IS NULL and cancel='No' ")
            cust=databaseConnection.cur.fetchall()
            if len(cust)>0:
                del self.cust_list[:]
                self.cust_list.append("Select")
                for i in cust:
                    self.cust_list.append(i[0]) 

            databaseConnection.cur.execute("Select name from registration where userType='Driver' and status= 'Available'")
            driv=databaseConnection.cur.fetchall()
            if len(driv)>0:
                del self.driv_list[:]
                self.driv_list.append("Select")
                for i in driv:
                    self.driv_list.append(i[0])

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    # =====================AssignDriver======================
    def AssignDriver(self):
        databaseConnection
        #  Find customerId
        databaseConnection.cur.execute("select c.c_id from customer c INNER JOIN booking b on c.c_id=b.c_id where c.name= (?)",(self.var_customer.get(),))
        customerId=databaseConnection.cur.fetchone()
        custID = functools.reduce(lambda sub, ele: sub * 10 + ele, customerId)
        print("C id=", custID)
        # #  Find driverId
        databaseConnection.cur.execute("select reg_id from registration  where name= ?",(self.var_driver.get(),))
        driverId=databaseConnection.cur.fetchone()
        # Convert Tuple to integer Using reduce() + lambda
        drivID = functools.reduce(lambda sub, ele: sub * 10 + ele, driverId)
        print("D id=", drivID)
        try:
            if self.var_driver.get() == "" or self.var_customer.get() == "":
                messagebox.showerror("Error", "All Field Must be required", parent=self.root)
            elif self.var_driver.get() == "Select" or self.var_customer.get() == "Select":
                messagebox.showerror("Error", "Please select the customer and driver!", parent=self.root)
            else:
                result=databaseConnection.cur.execute("Update booking set status='Conformed', reg_id=? where c_id=? and cancel='No'", (

                        drivID,
                        custID,
                        
                    ))
                databaseConnection.con.commit()
                

            if result:
                databaseConnection.cur.execute("Update registration set status='Unavailable' where reg_id=?", (
                    drivID,
                    ))
                databaseConnection.con.commit()
                messagebox.showinfo("Sucess", "Driver Assigned Sucessfully", parent=self.root)
                self.driverStatus()
                self.fetch_driver_Name()
                self.ViewTable()
                self.var_customer.set("Select")
                self.var_driver.set("Select")
                
            else:
                messagebox.showerror("Error","System Error", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)

    # =====================ShowBookedData======================
    def showConformed(self):
        databaseConnection
        try:
            databaseConnection.cur.execute("select booking.booking_id, booking.picDate,booking.dropDate, booking.picTime, booking.dropTime, booking.picAddress, booking.dropAddress, booking.status, registration.name, customer.name from booking  LEFT OUTER JOIN registration  on registration.reg_id=booking.reg_id JOIN customer  on customer.c_id=booking.c_id WHERE booking.status='Conformed'")
            rows = databaseConnection.cur.fetchall()
            # print(rows)
            self.RegistrationTable.delete(*self.RegistrationTable.get_children())
            for row in rows:
                self.RegistrationTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)


    # =====================ChangeDriverStatus======================
    def driverStatus(self):
        databaseConnection
        # #  Find driverId
        databaseConnection.cur.execute("select reg_id from registration  where name= (?)",(self.var_driver.get(),))
        driverId=databaseConnection.cur.fetchone()
        # Convert Tuple to integer Using reduce() + lambda
        drivID = functools.reduce(lambda sub, ele: sub * 10 + ele, driverId)
        print("D id=", drivID)
        try:
                databaseConnection.cur.execute("update registration set status='Unavailable' where reg_id=?", (

                        drivID,
                        
                    ))
                databaseConnection.con.commit()
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)


#==========MainMethod============           
if __name__=="__main__":
    root=Tk()
    obj=assignDriverClass(root)
    root.mainloop()