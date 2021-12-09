from tkinter import *
from tkinter import font
from tkinter.font import BOLD
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import functools
import os
import tempfile
import databaseConnection


#======================================================================GUI_Designing======================================================================================
class paymentClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("830x550+300+130")
        self.root.title("Manage Payment || TBS-Taxi Booking System || Developed By Sailesh Rokaya")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(0,0)
        
        #===========ProjectIcon=============
        photo = PhotoImage(file = "images/sales.png")
        self.root.iconphoto(False, photo)

        #================titel====================================
        title=Label(self.root, text="View Customer Bills", font=("goudy old style",20, "bold"),bg="#0f4d7d", fg="white").place(x=50,y=10, width=739,height=40)

        #================Variables===============================
        self.var_customer=StringVar()
        self.var_bill_No=StringVar()
        self.var_rate=IntVar()
        self.var_km=IntVar()
        self.var_total=IntVar()
        self.var_sc=IntVar()
        self.var_Vat=IntVar()
        self.var_G_total=IntVar()


        self.cust_list=[]
        self.fetch_cust_Name()
        # #===========TopFrame====================
        top_Frame=Frame(self.root, bd=2,relief=RIDGE,bg="white")
        top_Frame.place(x=50,y=55,width=740,height=60)

        #================Labels===================================
        lbl_Customer=Label(top_Frame, text="Customer Name", font=("times new roman", 15), bg="white").place(x=10, y=15)
        lbl_Rate=Label(top_Frame, text="Rate:", font=("times new roman", 15), bg="white").place(x=350, y=15)
        lbl_km=Label(top_Frame, text="Kilometer(KM):", font=("times new roman", 15), bg="white").place(x=530, y=15)
        #===============TextBox==============
        txtRate=Entry(top_Frame, textvariable=self.var_rate, font=("Andalus",10),bg="white", fg="#767171").place(x=410,y=15, width=80, height=30)
        txtDays=Entry(top_Frame, textvariable=self.var_km, font=("Andalus",10),bg="white", fg="#767171").place(x=680,y=15, width=50, height=30)

        #================BomboBox===================================
        cmb_Customer=ttk.Combobox(top_Frame, textvariable=self.var_customer, values=self.cust_list,state='readonly',justify=CENTER,font=("goudy old style",10))
        cmb_Customer.place(x=160, y=15,width=180,height=28)
        
         #===========ButtonFrame====================
        frmbtn=Frame(self.root, bd=2,relief=RIDGE,bg="white")
        frmbtn.place(x=400,y=455,width=390,height=60)
        #================Buttons===============================
        btn_total=Button(frmbtn,text="Total",command=self.billArea, font=("goudy old style",15), bg="#1CA345",fg="white",cursor="hand2").place(x=15,y=15,width=100,height=30)
        btn_generate=Button(frmbtn,text="Generate", command=self.GenerateBill,  font=("goudy old style",15), bg="#4caf50",fg="white",cursor="hand2").place(x=135,y=15,width=100,height=30)
        btn_print=Button(frmbtn,text="Print", command=self.printbill, font=("goudy old style",15), bg="#607d8b",fg="white",cursor="hand2").place(x=255,y=15,width=100,height=30)
        

        #===========BillFrame====================
        bill_Frame=Frame(self.root, bd=2,relief=RIDGE,bg="white")
        bill_Frame.place(x=50,y=120,width=325,height=400)
        #================titel====================================
        bill_title=Label(bill_Frame, text="Customer Bills", font=("goudy old style",20, "bold"),bg="orange").pack(side=TOP,fill=X)
        
        scroll_y = Scrollbar(bill_Frame,orient = VERTICAL)
        self.txt = Text(bill_Frame,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)
        
            
        #==============Image=====================
        self.bill_photo=Image.open("images/cat2.jpg")
        self.bill_photo=self.bill_photo.resize((450,300), Image.ANTIALIAS)
        self.bill_photo=ImageTk.PhotoImage(self.bill_photo)
        lbl_bill_phot=Label(self.root, image=self.bill_photo,bd=0)
        lbl_bill_phot.place(x=380, y=120)
        
    def ChangeBookingStatus(self):
        databaseConnection
        databaseConnection.cur.execute("select c.c_id from customer c INNER JOIN booking b on c.c_id=b.c_id where c.name=? and b.status='Closed'",(self.var_customer.get(),))
        customerId=databaseConnection.cur.fetchone()
        print("Cust Id:",customerId)
        # Convert Tuple to integer Using reduce() + lambda
        CustId = functools.reduce(lambda sub, ele: sub * 10 + ele, customerId)
        print("CustomerId: ", CustId)
        #  Find BookingId
        databaseConnection.cur.execute("SELECT booking_id FROM booking WHERE c_id=? and status='Closed'",(CustId,))
        bookingId=databaseConnection.cur.fetchone()
        bookId = functools.reduce(lambda sub, ele: sub * 10 + ele, bookingId)
        print("BookingId=",bookId)
        try:                                
            databaseConnection.cur.execute("Update booking set status='Paid' where booking_id=?",(bookId, ))
            databaseConnection.con.commit()

        except Exception as ex:messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)    
    
    # def findCustId(self):
    #     #  Find CustomerId
    #     global CustId
       
   
    # =====================GenerateBill======================
    def GenerateBill(self):
        databaseConnection.cur.execute("select c.c_id from customer c INNER JOIN booking b on c.c_id=b.c_id where c.name=? and b.status='Closed'",(self.var_customer.get(),))
        customerId=databaseConnection.cur.fetchone()
        print("Cust Id:",customerId)
        # Convert Tuple to integer Using reduce() + lambda
        CustId = functools.reduce(lambda sub, ele: sub * 10 + ele, customerId)
        print("CustomerId: ", CustId)
        Total=float((self.var_rate.get())*(self.var_km.get()))
        # print(Total)
        SC=float(Total*0.1)
        VAT=float((Total+SC)*0.13)
        Grand_Total=float(Total + SC + VAT)
        databaseConnection
        try:
            if self.var_customer.get() == "" or self.var_rate.get()=="" or self.var_km.get()=="":
                messagebox.showerror(
                    "Error", "Customer must be required", parent=self.root)
            else:
                databaseConnection.cur.execute("Select * from receipt where bill_No=?",(self.var_bill_No.get(),))
                row = databaseConnection.cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "Bill already exits, Try different", parent=self.root)
                else:
                    databaseConnection.cur.execute("Insert into receipt (rate,km,total,sc,vat,grandTotal,c_id) values (?,?,?,?,?,?,?)", (
                        self.var_rate.get(),
                        self.var_km.get(),
                        Total,
                        SC,
                        VAT,
                        Grand_Total,
                        CustId,               
                    ))
                    databaseConnection.con.commit()
                    self.ChangeBookingStatus()
                    messagebox.showinfo("Sucess", "Receipt Generate Sucessfully", parent=self.root)
                    self.billArea()
        except Exception as ex:
            pass

    #======================Function For Text Area========================
    def billArea(self):
        #  Find PhoneNumber
        databaseConnection.cur.execute("select c.telephone from customer c INNER JOIN booking b on c.c_id=b.c_id where c.name=? and b.status='Closed'",(self.var_customer.get(),))
        ContactNo=databaseConnection.cur.fetchone()
        print(ContactNo)
        # Convert Tuple to integer Using reduce() + lambda
        ContNo = functools.reduce(lambda sub, ele: sub * 10 + ele, ContactNo)
        print("Contact No: ", ContNo)
        databaseConnection.cur.execute("select c.c_id from customer c INNER JOIN booking b on c.c_id=b.c_id where c.name=? and b.status='Closed'",(self.var_customer.get(),))
        customerId=databaseConnection.cur.fetchone()
        print("Cust Id:",customerId)
        # Convert Tuple to integer Using reduce() + lambda
        CustId = functools.reduce(lambda sub, ele: sub * 10 + ele, customerId)
        print("CustomerId: ", CustId)
        # Find Bill No
        databaseConnection.cur.execute("select bill_No from receipt where c_id=?",(CustId,))
        billNo = databaseConnection.cur.fetchone()
        print(billNo)
        
        #Total,SC,VAT,G.total Calculation
        Total=float((self.var_rate.get())*(self.var_km.get()))
        # print(Total)
        SC=float(Total*0.1)
        VAT=float((Total+SC)*0.13)
        Grand_Total=float(Total + SC + VAT)
        self.txt.delete('1.0',END)
        self.txt.insert(END,"       Taxi Booking System\n")
        self.txt.insert(END,"         Kathmandu Nepal\n")
        if billNo:
            # Convert Tuple to integer Using reduce() + lambda
            billNo = functools.reduce(lambda sub, ele: sub * 10 + ele, billNo)
            print("Bill No is: ", billNo)
            
            # self.txt.insert(END,"             Invoice\n")
            # self.txt.insert(END,f"\nBill No. :  ")
        self.txt.insert(END,"           Tax Invoice\n")
        self.txt.insert(END,f"\nBill No. :  {billNo}")
        self.txt.insert(END,f"\nCustomer Name : {str(self.var_customer.get())}")
        self.txt.insert(END,f"\nPhone No. : {ContNo}")
        self.txt.insert(END,"\n=====================================")
        self.txt.insert(END,"\nParticulars      Kilometer      Rate")
        self.txt.insert(END,"\n=====================================")
        self.txt.insert(END,f"\nTaxi Service        {self.var_km.get()}km          {self.var_rate.get()}")
        self.txt.insert(END,"\n\n=====================================")
        self.txt.insert(END,f"\n                       Total:  {Total}")
        self.txt.insert(END,f"\n                     SC(10%):  {SC}")
        self.txt.insert(END,f"\n                    VAT(13%):  {VAT}")
        self.txt.insert(END,"\n                =====================")
        self.txt.insert(END,f"\n                 Grand Total:  {Grand_Total}")
        self.txt.insert(END,"\n\n\n\n             *Thank You*              ")
        
    #==========================Print Bill========================
    def printbill(self):
        new_file=tempfile.mktemp('.txt')
        open(new_file,'w').write(self.txt.get('1.0',END))
        os.startfile(new_file,'print')
    
       
     
        # =====================ShowData======================

    # def showBillNo(self):
    #     databaseConnection
    #     try:
    #         databaseConnection.cur.execute("select bill_No from receipt where c_id=2")
    #         billNo = databaseConnection.cur.fetchone()[0]
    #         print(billNo)
    #         # self.RegistrationTable.delete(*self.RegistrationTable.get_children())
    #         # for row in billNo:
    #         #     self.RegistrationTable.insert('', END, values=row)

    #     except Exception as ex:
    #         messagebox.showerror(
    #             "Error", f"Error due to : {str(ex)}", parent=self.root)
        
        
        

    #===================FetchDataInComboBox========
    def fetch_cust_Name(self):
        self.cust_list.append("Empty")
        databaseConnection
        try:
            databaseConnection.cur.execute("select c.name, c.c_id from customer c INNER JOIN booking b on c.c_id=b.c_id WHERE status='Closed' ")
            cust=databaseConnection.cur.fetchall()
            if len(cust)>0:
                del self.cust_list[:]
                self.cust_list.append("Select")
                for i in cust:
                    self.cust_list.append(i[0]) 

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

#==========MainMethod============           
if __name__=="__main__":
    root=Tk()
    obj=paymentClass(root)
    root.mainloop()