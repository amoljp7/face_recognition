from logging import PlaceHolder
from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image,ImageTk
import tkinter.messagebox
import mysql.connector
import re   
from face_recognition import Face_recog
from main import Face_Recognition_System
import cv2
import os
import numpy as np
from re import split
from time import strftime
from datetime import datetime

   
    
def main():
    Win1=Tk()
    Win= Starting_Win(Win1)

    Win1.mainloop()
    
class Starting_Win():
    def __init__(self,root1):


        
        self.root2=root1
        
           

        self.root2.title("Welcome to Attendance System using Face Recognition")
        self.root2.iconposition(x=0,y=0)
        self.root2.geometry("1950x1100+0+0")
        self.root2.configure(bg="white")
        #self.root2.iconbitmap(bitmap=r'1[495].ico')
            


        
       
        imgBG1=Image.open("D:/FDAP/face recognization/first.png")
        imgBG1=imgBG1.resize((1920,1050))
        self.BGI1=ImageTk.PhotoImage(imgBG1)
        lbl_bg1=Label(self.root2,image=self.BGI1)
        lbl_bg1.place(x=0,y=0,width=1920,height=1050)
        
        
        


        B1=Button(self.root2,command=self.Login_window,text="Login",bg="white",font=("Helvetica",13),bd=1,relief=RIDGE,fg="black",activeforeground="white",activebackground="white")
        B1.place(x=1800,y=30,width=100,height=35)
        
       
        

        b2_1=Button(self.root2,text="Attendance",cursor="hand2",command=self.face_data,font=("Arial Rounded MT Bold",25,"bold"),bg="purple",fg="white")
        b2_1.place(x=720,y=950,width=380,height=45)


        devlopername=Label(self.root2,text="Attendance System",font=("Arial Rounded MT Bold",25,"bold"),bg='purple',fg="white")
        devlopername.place(x=720,y=50,width=380,height=45)
        #for attendance system name on top of first page
   
        

    def Login_window(self):
        self.new_window2=Toplevel(self.root2)
        self.app=Login_Win(self.new_window2)

    def face_data(self):
        self.new_window=Toplevel(self.root2)
        self.app=Face_recog(self.new_window)


class Forget_Pass:
    def __init__(self,root):
        

        self.var_email=StringVar()
        self.var_otp=StringVar()
        self.var_new_pass=StringVar()
        self.root3=root
        
           

        self.root3.title("       ")
        self.root3.iconposition(x=0,y=0)
        self.root3.geometry("1950x1100+0+0")
        self.root3.configure(bg="white")
        #self.root3.iconbitmap(bitmap=r'1[495].ico')
            


        
       
        imgBG1=Image.open("D:/FDAP/face recognization/fpb.jpg")
        imgBG1=imgBG1.resize((1950,1100))
        self.BGI1=ImageTk.PhotoImage(imgBG1)
        lbl_bg1=Label(self.root3,image=self.BGI1)
        lbl_bg1.place(x=0,y=0,width=1950,height=1100)
        
        
        
        
        


        
        #Login
        lbl_login=Label(self.root3,text="Forget Password ?",font=("Arial Rounded MT Bold",25,"bold"),fg="white",bg="#30023F").place(x=825,y=230)
        
        #username
        lbl_email=Label( self.root3,text="Registered Phone Number :",font=("Helvetica",13),fg="white",bg="#30023F").place(x=720,y=350)
        
        self.email=ttk.Entry(self.root3,textvariable=self.var_email,font=("Helvetica",15))
        self.email.place(x=950,y=350)

        submitbutton1=Button(self.root3,text="Get OTP",command=self.OTP_gen,font=("Helvetica",13),bd=1,relief=RIDGE,fg="White",bg="#30023F",activeforeground="white",activebackground="black").place(x=1250,y=348,width=100,height=30)

    

        
        
        #password
        lbl_otp=Label(self.root3,text="OTP :",font=("Helvetica",13),fg="white",bg="#30023F").place(x=720,y=400)
       
        self.textotp=ttk.Entry(self.root3,textvariable=self.var_otp,show="*",font=("Helvetica",15))
        self.textotp.place(x=950,y=400)

            #password
        lbl_new_pass=Label(self.root3,text="New Password :",font=("Helvetica",13),fg="white",bg="#30023F").place(x=720,y=450)
        
        self.textnewpass=ttk.Entry(self.root3,textvariable=self.var_new_pass,show="*",font=("Helvetica",15))
        self.textnewpass.place(x=950,y=450)





            #loginbutton
            
        submitbutton1=Button(self.root3,text="Submit",font=("Helvetica",13),bd=1,relief=RIDGE,fg="White",bg="#30023F",activeforeground="white",activebackground="black").place(x=870,y=528,width=100,height=35)

    def OTP_gen(self):
        self.regexphoneno = re.compile("(0/91)?[7-9][0-9]{9}")
        self.regexpassword=re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,8}$")
        self.regexemail = re.compile('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')  

            
        if self.email.get()=="" or self.textotp.get()=="" or self.textnewpass=="":
            tkinter.messagebox.showwarning("Error","Please enter Registered mobile number",parent=self.root3)





        else:
            if self.regexemail.search(self.email.get()):

            
                conn=mysql.connector.connect(host="Localhost",user="root",password="",database="data")
                my_cur=conn.cursor()
                
                value=(self.email.get(),)
                my_cur.execute("select * from registration_table where email=%s",value)
                row=my_cur.fetchone()
                if row==None:
                    tkinter.messagebox.showerror("Error","Email is not Registered",parent=self.root3)
                else:

                    if self.regexpassword.search(self.var_new_pass.get()):
                        value=(self.var_new_pass.get(),self.email.get())
                        my_cur.execute("update registration_table set password=%s where email=%s",value)

                        conn.commit()
                        conn.close()
                        tkinter.messagebox.showinfo("Sucess","Password changed Sucessfully!!")


                        
                    else:
                        tkinter.messagebox.showerror("Error","Password should contain one capital letter-one number- one special character-length should be between 5-8",parent=self.root3)

            else:
                tkinter.messagebox.showerror("Error","Invalid Email format",parent=self.root3)
                
                    


                        
                        
                    
            


                    


                
                
        


        
    
   


        

    
        
    
    
    
        
        



            
    
    


class Login_Win:
     
    def __init__(self,root):
        

        self.var_username=StringVar()
        self.var_password=StringVar()
        self.root=root
        
           

        self.root.title("Login Page")
        self.root.iconposition(x=0,y=0)
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        self.root.configure(bg="white")
        #self.root.iconbitmap(bitmap=r'1[495].ico')
            


        
        imgBG1=Image.open("D:/FDAP/face recognization/login.jpg")
        imgBG1=imgBG1.resize((1950,1150))
        self.BGI1=ImageTk.PhotoImage(imgBG1)
        lbl_bg1=Label(self.root,image=self.BGI1)
        lbl_bg1.place(x=0,y=0,width=1950,height=1150)
        


        
        
        self.textuser1=ttk.Entry(self.root,textvariable=self.var_username,font=("Helvetica",20))
        self.textuser1.place(x=1180,y=520,width=600,height=65)
       
        imgu1=Image.open("D:/FDAP/face recognization/u.png")
        imgu1=imgu1.resize((50,50))
        self.u1=ImageTk.PhotoImage(imgu1)
        lbl_u1=Label(self.root,image=self.u1)
        lbl_u1.place(x=1105,y=527,width=50,height=50)
        

        
        
       
        self.textpass1=ttk.Entry(self.root,textvariable=self.var_password,show="*",font=("Helvetica",20))
        self.textpass1.place(x=1180,y=620,width=600,height=65)
        imgu2=Image.open("D:/FDAP/face recognization/pa.png")
        imgu2=imgu2.resize((50,50))
        self.u2=ImageTk.PhotoImage(imgu2)
        lbl_u2=Label(self.root,image=self.u2)
        lbl_u2.place(x=1105,y=627,width=50,height=50)
        

        #loginbutton
        loginbutton1=Button(self.root,command=self.Login_click,text="Login",font=("Arial Rounded MT Bold",20,BOLD),bd=1,relief=RIDGE,fg="purple",bg="white",activeforeground="white",activebackground="purple").place(x=1250,y=800,width=500,height=55)

        #registration
        registrationbutton1=Button(self.root,command=self.Register_window,text=" New User ? Sign Up",font=("Arial Rounded MT Bold",20,BOLD),borderwidth=0,fg="purple",bg="white",activebackground="purple").place(x=1190,y=720,width=600,height=55)

        #forgetpass
        #forgetpassbutton1=Button(self.root,text="Forget Password?",command=self.Forget_win,font=("Arial Rounded MT Bold",20,BOLD),borderwidth=0,fg="purple",bg="white",activebackground="purple").place(x=1470,y=720,width=300,height=55)

    def Register_window(self):


        self.new_window=Toplevel(self.root)
        self.app=Registartion(self.new_window)
        
    def Forget_win(self):
        self.new_window=Toplevel(self.root)
        self.app=Forget_Pass(self.new_window)

        
        

        
        

        



    







        
            
            
        

    
    
        




        
        


    


    def Login_click(self):
        
        if self.textuser1.get()=="" or self.textpass1.get()=="":
            tkinter.messagebox.showwarning("Error","all feild required",parent=self.root)





        else:
           

                conn=mysql.connector.connect(host="Localhost",user="root",password="12345",database="face_recognizer")
                my_cur=conn.cursor()
                my_cur.execute("select * from registration_table where username=%s and password=%s",(self.textuser1.get(),self.textpass1.get()))

                row=my_cur.fetchone()

                if row==None:
                    tkinter.messagebox.showwarning("Error","Wrong username or password",parent=self.root)

                else:

                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                    conn.commit()
                    conn.close()
                    
        
            







            
        
class Registartion:

    def __init__(self,root):
        #Window
        self.register=False
        self.root=root  
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        self.root.title("Registration Page")
        self.root.configure(bg="white")
        #self.root.iconbitmap(bitmap=r'1[495].ico')
        #Mudra
         
        imgBG1=Image.open("D:/FDAP/face recognization/bgr.jpg")
        imgBG1=imgBG1.resize((1950,1100))
        self.BGI1=ImageTk.PhotoImage(imgBG1)
        lbl_bg1=Label(self.root,image=self.BGI1)
        lbl_bg1.place(x=0,y=0,width=1950,height=1100)





        
        

         #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_email=StringVar()
        self.var_phoneno=StringVar()
        self.var_username=StringVar()
        self.var_password=StringVar()
        print(type(self.var_fname))
        self.Flag=False
        self.c=0
        




     
        

        #registartion
        lbl_Regi=Label(self.root,text="A D M I N  S I G N  U P",font=("Arial Rounded MT Bold",20,BOLD),fg="white",bg="#440B74").place(x=864,y=100)

        #Adminname

    #FirstName
        lbl_AdminFName=Label(self.root,text="Admin First Name :",font=("Arial Rounded MT Bold",13,BOLD),fg="white",bg="#440B74").place(x=553,y=230)
        
        self.AdminFName=ttk.Entry(self.root,textvariable=self.var_fname,font=("Helvetica",14))
        self.AdminFName.place(x=730,y=230)
        


    #Lastname 
        lbl_AdminLName=Label(self.root,text="Admin Last Name :",font=("Arial Rounded MT Bold",13,BOLD),fg="white",bg="#440B74").place(x=980,y=230)
        
        self.AdminLName=ttk.Entry(self.root,textvariable=self.var_lname,font=("Helvetica",14))
        self.AdminLName.place(x=1170,y=230)


        #Email
        lbl_Email=Label(self.root,text="Email Id :",font=("Arial Rounded MT Bold",13,BOLD),fg="white",bg="#440B74").place(x=553,y=330)
        
        self.Email=ttk.Entry(self.root,textvariable=self.var_email,font=("Helvetica",14))
        self.Email.place(x=730,y=330)

        #phoenno
        lbl_Phoneno=Label(self.root,text="Phone Number :",font=("Arial Rounded MT Bold",13,BOLD),fg="white",bg="#440B74").place(x=980,y=330)
        
        self.Phoneno=ttk.Entry(self.root,textvariable=self.var_phoneno,font=("Helvetica",14))
        self.Phoneno.place(x=1170,y=330)

        #username
        lbl_Usernamer=Label(self.root,text="Username :",font=("Arial Rounded MT Bold",13,BOLD),fg="white",bg="#440B74").place(x=553,y=430)
        
        self.Usernamer=ttk.Entry(self.root,textvariable=self.var_username,font=("Helvetica",14))
        self.Usernamer.place(x=730,y=430)

        #password
        lbl_Passwordr=Label(self.root,text="Password : ",font=("Arial Rounded MT Bold",13,BOLD),fg="white",bg="#440B74").place(x=980,y=430)
        
        self.Passwordr=ttk.Entry(self.root,textvariable=self.var_password,show="*",font=("Helvetica",14))
        self.Passwordr.place(x=1170,y=430)

        #Register

        
        registerbutton=Button(self.root,command=self.register_data,text="Register",font=("Arial Rounded MT Bold",20,BOLD),bd=1,relief=RIDGE,fg="White",bg="#440B74",activeforeground="black",activebackground="#5A128F").place(x=910,y=540,width=200,height=35)
        
    def register_data(self):
        self.ID=0
        self.regexemail = re.compile('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')  
        self.regex_name = re.compile(r'([a-z]+)( [a-z]+)*( [a-z]+)*$', 
              re.IGNORECASE)
        self.regexphoneno = re.compile("(0/91)?[7-9][0-9]{9}")
        self.regexpassword=re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,8}$")


        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_email.get()=="" or self.var_phoneno.get()==None or self.var_username.get()=="" or self.var_password.get()=="" :
            tkinter.messagebox.showerror("Error","All Field Are Requried",parent=self.root)
            self.root.destroy()
       
            
        else:
            if self.Validate_Form()==4  :


            
                conn=mysql.connector.connect(host="Localhost",user="root",password="12345",database="face_recognizer")
                my_cur=conn.cursor()
                query=("select * from registration_table where email=%s")
                value=(self.var_email.get(),)
                my_cur.execute(query,value)
                row=my_cur.fetchone()
                if row!=None:

                    tkinter.messagebox.showerror("Error","User Already exist",parent=self.root)
                  
                    

                
                else:
                    print(row)
                    try:
                        my_cur.execute("insert into registration_table values(%s,%s,%s,%s,%s,%s,%s)",(self.ID,
                                                                                self.var_fname.get(),
                                                                                self.var_lname.get(),
                                                                                self.var_email.get(),
                                                                                self.var_phoneno.get(),
                                                                                self.var_username.get(),
                                                                                self.var_password.get()
                                                                            ))
                        self.root.destroy()
                        conn.commit()
                        conn.close()
                        self.ID=self.ID+1

                        tkinter.messagebox.showinfo("sucess","Registered sucessfully")
                    except Exception as es:
                        tkinter.messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)    
        
                    
                    
                        
                
        
                

                

            

            
            
 


    def Validate_Form(self):
        self.c2=0

        if not(self.Flag):
            if self.regex_name.search(self.var_fname.get()) and self.regex_name.search(self.var_lname.get()) and self.regex_name.search(self.var_username.get()):
                self.c=self.c+1

                
            else:
                self.c2=self.c2+1
                tkinter.messagebox.showerror("Error","Match the format of Email or  Name or username",parent=self.root)
                

            if self.regexphoneno.match(self.var_phoneno.get()):
                self.c=self.c+1
                
            else:
                self.c2=self.c2+1
                tkinter.messagebox.showerror("Error","Match the format of Phone Number",parent=self.root)
                

            if self.regexpassword.search(self.var_password.get()):
                self.c=self.c+1
            else:
                self.c2=self.c2+1
                tkinter.messagebox.showerror("Error","Password should contain atleast one capital letter-one small letter-one number- one special character-length should be between 5-8",parent=self.root)
    
            if self.regexemail.search(self.var_email.get()):
                self.c=self.c+1
                
            else:
                self.c2=self.c2+1
                tkinter.messagebox.showerror("Error","Invalid Email",parent=self.root)
            if(self.c2>0):  
                self.c2=0
                self.root.destroy()

        return self.c



        
        

        

        




                


                








        
            


if __name__ == "__main__":
    main()

    
   
    

                    
    







        
       
        
     
        







      









        
           
            
        
            



           
        





        


        
