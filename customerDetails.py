from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk
from tkinter import messagebox
import databaseConnection

#======================================================================GUI_Designing======================================================================================
class customerDetailsClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1100x500+300+130")
        self.root.title("Customer Details || TBS-Taxi Booking System || Developed By Sailesh Rokaya")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(0,0)

        # ===========================All Variables===========
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_c_id=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_telephone=StringVar()
        self.var_password=StringVar()
        self.var_creditCard=StringVar()
        
        
        #===========ProjectIcon=============
        photo = PhotoImage(file = "images/customer.png")
        self.root.iconphoto(False, photo)

        #===============SearchFrame=========================
        SearchFrame=LabelFrame(self.root, text="Search Customer", font=("goudy old style",12,"bold"), bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x=250, y=20, width=600, height=70)

        #===============ComboBoxOptions=======================
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby, values=("Select","Email","Name","Telephone"),state='readonly',justify=CENTER,font=("goudy old style",10))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        #================Textbox===============================
        txt_search=Entry(SearchFrame, textvariable=self.var_searchtxt,font=("goudy old style",15), bg="lightyellow").place(x=200,y=10)

        #================Btn_Search===============================
        btn_search=Button(SearchFrame,text="Search",command=self.search, font=("goudy old style",15), bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

        #================titel====================================
        title=Label(self.root, text="Customer Details", font=("goudy old style",15),bg="#0f4d7d", fg="white").place(x=50,y=100, width=1000)

    #================Content=======================================
        #================Labels-Row-1====================================
        lbl_custId=Label(self.root, text="Cust. ID", font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_gender=Label(self.root, text="Gender", font=("goudy old style",15),bg="white").place(x=390,y=150)
        lbl_telephone=Label(self.root, text="Telephone", font=("goudy old style",15),bg="white").place(x=750,y=150)


        #================TextFields-Row-1====================================
        txt_custId=Entry(self.root, textvariable=self.var_c_id, stat="disable", font=("goudy old style",15),bg="lightyellow").place(x=150,y=150, width=180)
        txt_telephone=Entry(self.root, textvariable=self.var_telephone, font=("goudy old style",15),bg="lightyellow").place(x=850,y=150, width=180)

        #===============ComboBoxForGender-Row-1==============================
        txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender, values=("Select","Male","Female","Others"),state='readonly',justify=CENTER,font=("goudy old style",10))
        txt_gender.place(x=500,y=150, width=180)
        txt_gender.current(0)


        #================Labels-Row-2====================================
        lbl_name=Label(self.root, text="Name", font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_email=Label(self.root, text="Email", font=("goudy old style",15),bg="white").place(x=390,y=190)
        lbl_password=Label(self.root, text="Password", font=("goudy old style",15),bg="white").place(x=750,y=190)


        #================TextFields-Row-2====================================
        txt_name=Entry(self.root, textvariable=self.var_name, font=("goudy old style",15),bg="lightyellow").place(x=150,y=190, width=180)
        txt_email=Entry(self.root, textvariable=self.var_email, font=("goudy old style",15),bg="lightyellow").place(x=500,y=190, width=180)
        txt_password=Entry(self.root, textvariable=self.var_password, show="*", font=("goudy old style",15),bg="lightyellow").place(x=850,y=190, width=180)

        #================Labels-Row-3====================================
        lbl_card=Label(self.root, text="Card Details", font=("goudy old style",15),bg="white").place(x=500,y=230)
        
        #===============ComboBoxForUserType-Row-3==============================
        txt_card=Entry(self.root, textvariable=self.var_creditCard, font=("goudy old style",15),bg="lightyellow").place(x=620,y=230, width=180)
        
        #================Labels-Row-4====================================
        lbl_address=Label(self.root, text="Address", font=("goudy old style",15),bg="white").place(x=50,y=230)

        #================TextFields-Row-4====================================
        self.txt_address=Text(self.root,  font=("goudy old style",15),bg="lightyellow")
        self.txt_address.place(x=150,y=230, width=300, height=75)

        #================Buttons===============================
        btn_add=Button(self.root,text="Save",command=self.add, font=("goudy old style",15), bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=265,width=110,height=40)
        btn_update=Button(self.root,text="Update",command=self.update, font=("goudy old style",15), bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=265,width=110,height=40)
        btn_delete=Button(self.root,text="Delete",command=self.delete, font=("goudy old style",15), bg="#f44336",fg="white",cursor="hand2").place(x=740,y=265,width=110,height=40)
        btn_clear=Button(self.root,text="Clear",command=self.clear, font=("goudy old style",15), bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=265,width=110,height=40)


        #=================Customer Details======================
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=320,relwidth=1,height=180)
        #=================Scrollbar=============================
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
                                                        
        self.RegistrationTable=ttk.Treeview(emp_frame,columns=("c_id","name","address","gender","email","telephone","password","userType","creditCard"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.RegistrationTable.xview)
        scrolly.config(command=self.RegistrationTable.yview)
        
        self.RegistrationTable.heading("c_id",text="Customer ID")
        self.RegistrationTable.heading("name",text="Name")
        self.RegistrationTable.heading("address",text="Address")
        self.RegistrationTable.heading("gender",text="Gender")
        self.RegistrationTable.heading("email",text="Email")
        self.RegistrationTable.heading("telephone",text="Telephone")
        self.RegistrationTable.heading("password",text="Password")
        self.RegistrationTable.heading("userType",text="UserType")
        self.RegistrationTable.heading("creditCard",text="Card Details")

        self.RegistrationTable["show"]="headings"
        self.RegistrationTable.column("c_id",width=60)
        self.RegistrationTable.column("name",width=100)
        self.RegistrationTable.column("address",width=130)
        self.RegistrationTable.column("gender",width=100)
        self.RegistrationTable.column("email",width=100)
        self.RegistrationTable.column("telephone",width=100)
        self.RegistrationTable.column("password",width=100)
        self.RegistrationTable.column("userType",width=100)
        self.RegistrationTable.column("creditCard",width=100)

        self.RegistrationTable.pack(fill=BOTH,expand=1)
        self.RegistrationTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    
    # ======================================================================DatabaseConnection======================================================================================

    # =====================Save======================
    def add(self):
        databaseConnection
        try:
            if self.var_name.get() == "" or self.var_email.get()=="" or self.var_password.get()=="":
                messagebox.showerror(
                    "Error", "Name,Email,Password Must be required", parent=self.root)
            else:
                databaseConnection.cur.execute("Select * from customer where email=?",(self.var_email.get(),))
                row = databaseConnection.cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "This email-id already exits, Try different", parent=self.root)
                else:
                    databaseConnection.cur.execute("Insert into customer (name,address,gender,email,telephone,password,userType,creditCard) values (?,?,?,?,?,?,'Customer',?)", (

                        
                        self.var_name.get(),
                        self.txt_address.get('1.0', END),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_telephone.get(),
                        self.var_password.get(),
                        self.var_creditCard.get()
                        
                    ))
                    databaseConnection.con.commit()
                    messagebox.showinfo(
                        "Sucess", "Customer Added Sucessfully", parent=self.root)
                    self.clear()
                    self.show()
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)

    # =====================ShowData======================

    def show(self):
        databaseConnection
        try:
            databaseConnection.cur.execute("select * from customer where userType='Customer'")
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
        f = self.RegistrationTable.focus()
        content = (self.RegistrationTable.item(f))
        row = content['values']
        self.var_c_id.set(row[0]),
        self.var_name.set(row[1]),
        self.txt_address.delete('1.0', END),
        self.txt_address.insert(END,row[2]),
        self.var_gender.set(row[3]),
        self.var_email.set(row[4]),
        self.var_telephone.set(row[5]),
        self.var_password.set(row[6]),
        self.var_creditCard.set(row[8])
        

    # =====================Update======================

    def update(self):
        databaseConnection
        try:
            if self.var_c_id.get() == "":
                messagebox.showerror(
                    "Error", "Customer ID Must be required", parent=self.root)
            else:
                databaseConnection.cur.execute("Select * from customer where c_id=?",
                            (self.var_c_id.get(),))
                row = databaseConnection.cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid Customer ID.", parent=self.root)
                else:
                    databaseConnection.cur.execute("Update customer set name=?,address=?,gender=?,email=?,telephone=?,password=?,userType='Customer',creditCard=? where c_id=?", (

                        self.var_name.get(),
                        self.txt_address.get('1.0', END),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_telephone.get(),
                        self.var_password.get(),
                        self.var_creditCard.get(),
                        self.var_c_id.get(),
                    ))
                    databaseConnection.con.commit()
                    messagebox.showinfo(
                        "Sucess", "Customer Updated Sucessfully", parent=self.root)
                    print(self.var_c_id.get())
                    self.clear()
                    self.show()
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)

    # =====================Delete======================

    def delete(self):
        databaseConnection
        try:
            if self.var_c_id.get() == "":
                messagebox.showerror(
                    "Error", "Customer ID Must be required", parent=self.root)
            else:
                databaseConnection.cur.execute("Select * from customer where c_id=?",
                            (self.var_c_id.get(),))
                row = databaseConnection.cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid Customer ID.", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Do you want to delete?", parent=self.root)
                    if op == True:
                        databaseConnection.cur.execute("delete from customer where c_id=?",
                                    (self.var_c_id.get(),))
                        databaseConnection.con.commit()
                        messagebox.showinfo(
                            "Delete", "Customer Delete Successfully", parent=self.root)
                        self.clear()
                        self.show()

        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)

    # =====================Clear======================

    def clear(self):
        self.var_c_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_telephone.set(""),
        self.var_password.set(""),
        self.var_creditCard.set(""),
        self.txt_address.delete('1.0', END),
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")

        self.show()

    # =====================Search======================

    def search(self):
        databaseConnection
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror(
                    "Error", "Select Search By Option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror(
                    "Error", "Search input should be required.", parent=self.root)
            else:
                databaseConnection.cur.execute("select * from customer where " + 
                            self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = databaseConnection.cur.fetchall()
                if len(rows) != 0:
                    self.RegistrationTable.delete(
                        *self.RegistrationTable.get_children())
                    for row in rows:
                        self.RegistrationTable.insert('', END, values=row)
                else:
                    messagebox.showerror(
                        "Error", "No record found!!!", parent=self.root)

        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)



#==========MainMethod============           
if __name__=="__main__":
    root=Tk()
    obj=customerDetailsClass(root)
    root.mainloop()
    