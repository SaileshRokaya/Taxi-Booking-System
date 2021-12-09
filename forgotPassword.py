from tkinter import *
from tkinter.font import BOLD
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import databaseConnection


#======================================================================GUI_Designing======================================================================================
class forgotPasswordClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("350x450+550+150")
        self.root.title("Forgot Password || TBS-Taxi Booking System || Developed By Sailesh Rokaya")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(0,0)

        # ===========================All Variables===========
        self.var_utype=StringVar()
        self.var_email = StringVar()
        self.var_NewPassword=StringVar()
        self.var_ConfNewPassword=StringVar()

        
        #===========ProjectIcon=============
        photo = PhotoImage(file = "images/logo.png")
        self.root.iconphoto(False, photo)

        #=============ForgotFrame===========
        Frame_forgot=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        Frame_forgot.place(x=5, y=10, width=340, height=435)

        #================titel====================================
        title=Label(Frame_forgot, text="Forgot Password", font=("goudy old style",20, "bold"),bg="#0f4d7d", fg="white").pack(side=TOP,fill=X)

        #===============ComboBoxForGender-Row-1==============================
        txt_Utype=ttk.Combobox(Frame_forgot,textvariable=self.var_utype, values=("Select UserType","Customer","Driver","Employee"),state='readonly',justify=CENTER,font=("Andalus",10))
        txt_Utype.place(x=60,y=60, width=200, height=30)
        txt_Utype.current(0)

        #===============Label==============
        lbl_email=Label(Frame_forgot,text="Email*",bg="white", font=("Andalus",15), fg="#767171").place(x=0,y=120, relwidth=1)
        lbl_NewPassword=Label(Frame_forgot,text="New Password*", bg="white", font=("Andalus",15), fg="#767171").place(x=0,y=200,relwidth=1)
        lbl_ConfNewPassword=Label(Frame_forgot,text="Confirm New Password*", bg="white", font=("Andalus",15), fg="#767171").place(x=2,y=280,relwidth=1)
        
        #===============TextBox==============
        txtemail=Entry(Frame_forgot, textvariable=self.var_email, font=("Andalus",10),bg="white", fg="#767171").place(x=65,y=160, width=200, height=30)
        txtNewpassword=Entry(Frame_forgot, textvariable=self.var_NewPassword, font=("Andalus",10), bg="white", show="*", fg="#767171").place(x=65,y=240, width=200, height=30)
        txtConpassword=Entry(Frame_forgot, textvariable=self.var_ConfNewPassword, font=("Andalus",10), bg="white", show="*", fg="#767171").place(x=65,y=320, width=200, height=30)

        #============btn_logout=========
        btn_update=Button(Frame_forgot, text="Update!", command=self.forgotPasswordFunc, font=("time new roman", 15, "bold"), fg='white', activeforeground='white', bg="#418BCA",activebackground="#418BCA", cursor="hand2").place(x=65,y=370, height=35, width=200)
       

    def forgotPasswordFunc(self):
        email = self.var_email.get()
        newPassword= self.var_NewPassword.get()
        ConfNewPassword=self.var_ConfNewPassword.get()
        # password = self.var_password.get()
         # Find user If there is any take proper action
        try:
            if self.var_utype.get()=="Select UserType":
                messagebox.showwarning("Error","User Type must be requird!")
            elif self.var_utype.get()=="Employee":
                find_emp = ('SELECT * FROM registration WHERE email = ? and userType = "Employee"')
                databaseConnection.cur.execute(find_emp, [email])
                resultEmp = databaseConnection.cur.fetchall()
            elif self.var_utype.get()=="Driver":
                find_driver = ('SELECT * FROM registration WHERE email = ?  and userType = "Driver"')
                databaseConnection.cur.execute(find_driver, [email])
                resultDriv = databaseConnection.cur.fetchall()
            elif self.var_utype.get()=="Customer":
                find_cus = ('SELECT * FROM customer WHERE email = ? ')
                databaseConnection.cur.execute(find_cus, [email])
                resultCus = databaseConnection.cur.fetchall()
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)
 
        try:
            if email == "" or newPassword=="" or ConfNewPassword=="":
                messagebox.showerror("Error", "All Field Must be required", parent=self.root)
            elif newPassword != ConfNewPassword:
                messagebox.showerror("Error","**Password are not matching!")
            
            elif self.var_utype.get()=="Employee" and resultEmp and newPassword == ConfNewPassword:
                databaseConnection.cur.execute("Update registration set password=? where email= ?",(newPassword, email,))
                databaseConnection.con.commit()
                messagebox.showinfo("Password Updated!", "Successfully your password has been changed. \n Use your new password to log in.")
                self.clear()
            elif self.var_utype.get()=="Driver" and resultDriv and newPassword == ConfNewPassword:
                databaseConnection.cur.execute("Update registration set password=? where email= ?",(newPassword,email,))
                databaseConnection.con.commit()
                messagebox.showinfo("Password Updated!", "Successfully your password has been changed. \n Use your new password to log in.")
                self.clear()
            elif self.var_utype.get()=="Customer" and resultCus and newPassword == ConfNewPassword:
                databaseConnection.cur.execute("Update customer set password=? where email= ?",(newPassword,email,))
                databaseConnection.con.commit()
                messagebox.showinfo("Password Updated!", "Successfully your password has been changed. \n Use your new password to log in.")
                self.clear()

            else:
                messagebox.showerror("Error", "Invalid email !!!")

        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)
    
    def clear(self):
        self.var_utype.set("Select UserType")
        self.var_email.set("")
        self.var_NewPassword.set("")
        self.var_ConfNewPassword.set("")

#==========MainMethod============           
if __name__=="__main__":
    root=Tk()
    obj=forgotPasswordClass(root)
    root.mainloop()