from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk
from tkinter import messagebox
import databaseConnection

#======================================================================GUI_Designing======================================================================================
class customerRegClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("740x440+350+180")
        self.root.title("Customer Registration || TBS-Taxi Booking System || Developed By Sailesh Rokaya")
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
        
        
        # self.var_userType=StringVar()
        
        #===========ProjectIcon=============
        photo = PhotoImage(file = "images/customer.png")
        self.root.iconphoto(False, photo)

        #===============Frame=========================
        frm=LabelFrame(self.root,  font=("goudy old style",12,"bold"), bd=2, relief=RIDGE, bg="white")
        frm.place(x=10, y=10, width=720, height=420)

        #================titel====================================
        title=Label(frm, text="Customer Registration", font=("goudy old style",20),bg="#0f4d7d", fg="white").place(x=30,y=20, width=660)

    #================Content=======================================
        #================Labels-Row-1====================================
        lbl_name=Label(frm, text="Name", font=("goudy old style",15),bg="white").place(x=32,y=80)
        lbl_email=Label(frm, text="Email", font=("goudy old style",15),bg="white").place(x=390,y=80)
        
        #================TextFields-Row-1====================================
        txt_name=Entry(frm, textvariable=self.var_name, font=("goudy old style",15),bg="lightyellow").place(x=150,y=80, width=180)
        txt_email=Entry(frm, textvariable=self.var_email, font=("goudy old style",15),bg="lightyellow").place(x=500,y=80, width=180)
        
 
        #================Labels-Row-2====================================
        lbl_telephone=Label(frm, text="Telephone", font=("goudy old style",15),bg="white").place(x=32,y=150)
        lbl_password=Label(frm, text="Password", font=("goudy old style",15),bg="white").place(x=390,y=150)
        
        #================TextFields-Row-2====================================
        txt_telephone=Entry(frm, textvariable=self.var_telephone, font=("goudy old style",15),bg="lightyellow").place(x=150,y=150, width=180)
        txt_password=Entry(frm, textvariable=self.var_password, show="*", font=("goudy old style",15),bg="lightyellow").place(x=500,y=150, width=180)
        
        #================Labels-Row-3====================================
        lbl_card=Label(frm, text="Card Dets.", font=("goudy old style",15),bg="white").place(x=32,y=230)
        lbl_gender=Label(frm, text="Gender", font=("goudy old style",15),bg="white").place(x=390,y=230)
        #===============ComboBoxForGender-Row-3==============================
        txt_gender=ttk.Combobox(frm,textvariable=self.var_gender, values=("Select","Male","Female","Others"),state='readonly',justify=CENTER,font=("goudy old style",10))
        txt_gender.place(x=500,y=230, width=180)
        txt_gender.current(0)
        #================TextFields-Row-3====================================
        txt_card=Entry(frm, textvariable=self.var_creditCard, font=("goudy old style",15),bg="lightyellow").place(x=150,y=230, width=180)
        #================Labels-Row-4====================================
        lbl_address=Label(frm, text="Address", font=("goudy old style",15),bg="white").place(x=32,y=310)
        #================TextFields-Row-4====================================
        self.txt_address=Text(frm,  font=("goudy old style",15),bg="lightyellow")
        self.txt_address.place(x=150,y=310, width=300, height=75)

        #================Buttons===============================
        btn_add=Button(frm,text="Register",command=self.add, font=("goudy old style",15), bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=340,width=110,height=40)


    
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
                        "Sucess", "New User Added Sucessfully", parent=self.root)
                    self.clear()
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

#==========MainMethod============           
if __name__=="__main__":
    root=Tk()
    obj=customerRegClass(root)
    root.mainloop()