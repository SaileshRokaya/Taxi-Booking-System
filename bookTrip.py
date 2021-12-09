# from customerRegistration import customerRegClass
from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk
from tkinter import messagebox
import datetime
from tkcalendar import Calendar, DateEntry
import databaseConnection
# from Welcompage import *
 

#======================================================================GUI_Designing======================================================================================
class bookTripClass:
    def __init__(self, root, email):
        self.root=root
        self.root.geometry("720x450+350+180")
        self.root.title("Book Trip (Reservation) || TBS-Taxi Booking System || Developed By Sailesh Rokaya")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(0,0)
        
        # ===========================All Variables===========

        self.var_BookId=StringVar()
        self.var_PickUpDate=StringVar()
        self.var_DropDate=StringVar()
        self.var_PickupTime=StringVar()
        self.var_DropTime=StringVar()
        self.var_picAddress=StringVar()
        self.var_dropAddress=StringVar()
        self.email=email
        print(self.email)
        
        #===========ProjectIcon=============
        photo = PhotoImage(file = "images/taxitrip.png")
        self.root.iconphoto(False, photo)

        #================titel====================================
        title=Label(self.root, text="New Booking", font=("goudy old style",20, "bold"),bg="#0f4d7d", fg="white").place(x=20,y=15, width=680)

        #==============PickUpFrame======================
        frmPickUp=LabelFrame(self.root, text="Pick-Up", font=("goudy old style",12,"bold"), bd=2, relief=RIDGE, bg="white")
        frmPickUp.place(x=20, y=70, width=335, height=200)

        #==============DropFrame======================
        frmDrop=LabelFrame(self.root, text="Drop", font=("goudy old style",12,"bold"), bd=2, relief=RIDGE, bg="white")
        frmDrop.place(x=370, y=70, width=335, height=200)


    #================Content=======================================
        #================Label====================================
        lblWelcome=Label(self.root, text="Welcome: "+email, font=("goudy old style",10,"bold"),bg="white").place(x=530,y=55)
        lbl_PickUpDate=Label(frmPickUp, text="Date", font=("goudy old style",15),bg="white").place(x=10,y=5)
        lbl_DropDate=Label(frmDrop, text="Date", font=("goudy old style",15),bg="white").place(x=10,y=5)
        lbl_pickupTime=Label(frmPickUp, text="Time", font=("goudy old style",15),bg="white").place(x=10,y=60)
        lbl_dropTime=Label(frmDrop, text="Time", font=("goudy old style",15),bg="white").place(x=10,y=60)
        lbl_pickupAdd=Label(frmPickUp, text="Address", font=("goudy old style",15),bg="white").place(x=10,y=115)
        lbl_dropAdd=Label(frmDrop, text="Address", font=("goudy old style",15),bg="white").place(x=10,y=115)
        #================TextFields====================================
        txt_pickupTime=Entry(frmPickUp, textvariable=self.var_PickupTime, font=("goudy old style",15),bg="lightyellow").place(x=120,y=60, width=100)
        txt_dropTime=Entry(frmDrop, textvariable=self.var_DropTime, font=("goudy old style",15),bg="lightyellow").place(x=120,y=60, width=100)
        txt_PickUpAddress=Entry(frmPickUp, textvariable=self.var_picAddress,  font=("goudy old style",15),bg="lightyellow").place(x=120,y=115, width=180)
        txt_DropAddress=Entry(frmDrop, textvariable=self.var_dropAddress,  font=("goudy old style",15),bg="lightyellow").place(x=120,y=115, width=180)
        #================DateCalender====================================
        calPickUp=DateEntry(frmPickUp, textvariable=self.var_PickUpDate, font=("goudy old style",15),bg="lightyellow").place(x=120, y=10, width=100)
        calDrop=DateEntry(frmDrop, textvariable=self.var_DropDate, font=("goudy old style",15),bg="lightyellow").place(x=120, y=10, width=100)

        #================Buttons===============================
        btn_add=Button(self.root,text="Save", command=self.add, font=("goudy old style",15), bg="#2196f3",fg="white",cursor="hand2").place(x=370,y=275,width=70,height=30)
        btn_update=Button(self.root,text="Update", command=self.update, font=("goudy old style",15), bg="#4caf50",fg="white",cursor="hand2").place(x=450,y=275,width=70,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete, font=("goudy old style",15), bg="#f44336",fg="white",cursor="hand2").place(x=530,y=275,width=70,height=30)
        btn_clear=Button(self.root,text="Clear",command=self.clear, font=("goudy old style",15), bg="#607d8b",fg="white",cursor="hand2").place(x=610,y=275,width=70,height=30)

         #=================Customer Details======================
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=310,relwidth=1,height=150)
        #=================Scrollbar=============================
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
                                                        
        self.RegistrationTable=ttk.Treeview(emp_frame,columns=("booking_id","picDate","dropDate","picTime","dropTime","picAddress","dropAddress"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.RegistrationTable.xview)
        scrolly.config(command=self.RegistrationTable.yview)
        
        self.RegistrationTable.heading("booking_id",text="Booking ID")
        self.RegistrationTable.heading("picDate",text="Pick-Up Date")
        self.RegistrationTable.heading("dropDate",text="Drop Date")
        self.RegistrationTable.heading("picTime",text="Pick-Up Time")
        self.RegistrationTable.heading("dropTime",text="Drop Time")
        self.RegistrationTable.heading("picAddress",text="Pick-Up Address")
        self.RegistrationTable.heading("dropAddress",text="Drop Address")
      
        
        self.RegistrationTable["show"]="headings"
        self.RegistrationTable.column("booking_id",width=80)
        self.RegistrationTable.column("picDate",width=100)
        self.RegistrationTable.column("dropDate",width=100)
        self.RegistrationTable.column("picTime",width=100)
        self.RegistrationTable.column("dropTime",width=100)
        self.RegistrationTable.column("picAddress",width=100)
        self.RegistrationTable.column("dropAddress",width=100)
        
        
        self.RegistrationTable.pack(fill=BOTH,expand=1)
        self.RegistrationTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    # ======================================================================DatabaseConnection======================================================================================

    # # =====================Save======================
    
    def add(self):
        print(self.email)
        databaseConnection
        #Find customerId
        find_customerId=("SELECT c_id from customer WHERE email = '%s'" % (self.email))
        databaseConnection.cur.execute(find_customerId)
        customerId=databaseConnection.cur.fetchone()[0]
        print(customerId)
        # New reservation
        try:
            if self.var_PickUpDate.get() == "" or self.var_DropDate.get()=="" or self.var_picAddress.get()=="" or self.var_dropAddress.get()=="":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                databaseConnection.cur.execute("INSERT INTO booking(picDate, dropDate, picTime, dropTime, picAddress, dropAddress, status,cancel, c_id) VALUES (?,?,?,?,?,?,'Pending','No',?)", (  
                        
                        self.var_PickUpDate.get(),
                        self.var_DropDate.get(),
                        self.var_PickupTime.get(),
                        self.var_DropTime.get(),
                        self.var_picAddress.get(),
                        self.var_dropAddress.get(),
                        customerId
                        
                        
                    ))
                databaseConnection.con.commit()
                messagebox.showinfo("Sucess", "New Booking Added Sucessfully", parent=self.root)
                self.clear()
                self.show()
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)

    # =====================ShowData======================
    def show(self):
        databaseConnection
        #Find customerId
        find_customerId=("SELECT c_id from customer WHERE email = '%s'" % (self.email))
        databaseConnection.cur.execute(find_customerId)
        customerId=databaseConnection.cur.fetchone()[0]
        try:
            databaseConnection.cur.execute("SELECT * from booking WHERE status='Pending' and cancel='No' and c_id = '%s'" % (customerId))
            rows = databaseConnection.cur.fetchall()
            # print(rows)
            self.RegistrationTable.delete(*self.RegistrationTable.get_children())
            for row in rows:
                self.RegistrationTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)  

    # =====================GetData======================
    def get_data(self, ev):
        databaseConnection
        #Find customerId
        find_customerId=("SELECT c_id from customer WHERE  email = '%s'" % (self.email))
        databaseConnection.cur.execute(find_customerId)
        customerId=databaseConnection.cur.fetchone()[0]
        f = self.RegistrationTable.focus()
        content = (self.RegistrationTable.item(f))
        row = content['values']
        self.var_BookId.set(row[0]),
        self.var_PickUpDate.set(row[1]),
        self.var_DropDate.set(row[2]),
        self.var_PickupTime.set(row[3]),
        self.var_DropTime.set(row[4]),
        self.var_picAddress.set(row[5]),
        self.var_dropAddress.set(row[6]),
        

        
    # =====================Update======================

    def update(self):
        databaseConnection
        #Find customerId
        find_customerId=("SELECT c_id from customer WHERE email = '%s'" % (self.email))
        databaseConnection.cur.execute(find_customerId)
        customerId=databaseConnection.cur.fetchone()[0]
        try:
            if self.var_BookId == "":
                messagebox.showerror(
                    "Error", "Booking ID Must be required", parent=self.root)
            else:
                databaseConnection.cur.execute("Select * from booking where booking_id = ?",(self.var_BookId.get(),))
                row = databaseConnection.cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid Booking ID.", parent=self.root)
                else:                                               #    picDate, dropDate, picTime, dropTime, picAddress, dropAddress, c_id
                    databaseConnection.cur.execute("Update booking set picDate=?,dropDate=?,picTime=?,dropTime=?,picAddress=?,dropAddress=?,c_id=? where booking_id=?", (


                        self.var_PickUpDate.get(),
                        self.var_DropDate.get(),
                        self.var_PickupTime.get(),
                        self.var_DropTime.get(),
                        self.var_picAddress.get(),
                        self.var_dropAddress.get(),
                        customerId,
                        self.var_BookId.get()
                    ))
                    databaseConnection.con.commit()
                    messagebox.showinfo(
                        "Sucess", "Booking Updated Sucessfully", parent=self.root)
                    self.clear()
                    self.show()
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)

    # =====================Delete======================

    def delete(self):
        databaseConnection
        try:
            if self.var_BookId.get() == "":
                messagebox.showerror(
                    "Error", "Booking ID Must be required", parent=self.root)
            else:
                databaseConnection.cur.execute("Select * from booking where cancel= 'No' and  booking_id=?",(self.var_BookId.get(),))
                row = databaseConnection.cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid Booking ID.", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Do you want to delete?", parent=self.root)
                    if op == True:
                        databaseConnection.cur.execute("Update booking set status='Canceled', Cancel='Yes' where booking_id=?",
                                    (self.var_BookId.get(),))
                        databaseConnection.con.commit()
                        messagebox.showinfo("Delete", "Booking Delete Successfully", parent=self.root)
                        self.clear()
                        self.show()

        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)




    # =====================Clear======================

    def clear(self):

        self.var_PickupTime.set(""),
        self.var_DropTime.set(""),
        self.var_picAddress.set(""),
        self.var_dropAddress.set(""),

        self.show()


#==========MainMethod============           
if __name__=="__main__":
    root=Tk()
    obj=bookTripClass(root)
    root.mainloop()