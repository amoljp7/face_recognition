from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from traindata import Traindata




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        self.root.title("Face Recognition System")
        self.root.iconposition(x=0,y=0)
       # self.root.iconbitmap(bitmap=r'1[495].ico')


        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_add=StringVar()
        self.var_city=StringVar()

        
        img=Image.open("D:/FDAP/face recognization/first.png")
        img=img.resize((1950,320),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1950,height=320)

        #bg img
        img1=Image.open("D:/FDAP/face recognization/first.png")
        img1=img1.resize((2000,800),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        s_lbl=Label(self.root,image=self.photoimg1)
        s_lbl.place(x=0,y=300,width=2000,height=760)

        title_lbl=Label(s_lbl,text="Employee Details",font=("Arial Rounded MT Bold",30,"bold"),bg="black",fg="#a976e3")
        title_lbl.place(x=0,y=0,width=2000,height=70)

        main_frame=Frame(s_lbl,bd=2,bg="white")
        main_frame.place(x=0,y=65,width=2000,height=1550)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Details",font=("Arial Rounded MT Bold",15,"bold"))
        Left_frame.place(x=10,y=20,width=900,height=660)

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=30,y=40,width=830,height=160)

        #dept
        dep_label=Label(current_course_frame,text="Department",font=("Arial Rounded MT Bold",10,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("Arial Rounded MT Bold",10,"bold"),state="readonly",width=17)
        dep_combo["values"]=("IT","HR","Development","Testing")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course year
        year_label=Label(current_course_frame,text="Experience in Year",font=("Arial Rounded MT Bold",10,"bold"),bg="white")
        year_label.grid(row=0,column=4,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("Arial Rounded MT Bold",10,"bold"),state="readonly",width=17)
        year_combo["values"]=("Fresher","1-5","6-10","11-15","15-20")
        year_combo.current(0)
        year_combo.grid(row=0,column=5,padx=2,pady=10,sticky=W)

        #Academic  year
        a_year_label=Label(current_course_frame,text="Job Title",font=("Arial Rounded MT Bold",10,"bold"),bg="white")
        a_year_label.grid(row=2,column=0,padx=10,sticky=W)

        a_year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("Arial Rounded MT Bold",10,"bold"),state="readonly",width=19)
        a_year_combo["values"]=("Developer","Designer","Manager","Director","Board-Member")
        a_year_combo.current(0)
        a_year_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        #semister
        semister_label=Label(current_course_frame,text="CTC",font=("Arial Rounded MT Bold",10,"bold"),bg="white")
        semister_label.grid(row=2,column=4,padx=10,sticky=W)

        semister_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("Arial Rounded MT Bold",10,"bold"),state="readonly",width=19)
        semister_combo["values"]=("4","6","8","10","12","14","16","18")
        semister_combo.current(0)
        semister_combo.grid(row=2,column=5,padx=2,pady=10,sticky=W)

        #class student info
        class_stu_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Employee Information",font=("Arial Rounded MT Bold",15,"bold"))
        class_stu_frame.place(x=30,y=230,width=830,height=400)

        #student id
        stu_id_label=Label(class_stu_frame,text="EmployeeID:",font=("Arial Rounded MT Bold",10,"bold"),bg="white")
        stu_id_label.grid(row=0,column=0,padx=10,sticky=W)

        stuID_entry=ttk.Entry(class_stu_frame,textvariable=self.var_id,width=20,font=("Arial Rounded MT Bold",10,"bold"))
        stuID_entry.grid(row=0,column=1,padx=10,sticky=W)


        #student name
        stu_name_label=Label(class_stu_frame,text="Name:",font=("Arial Rounded MT Bold",10,"bold"),bg="white")
        stu_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        stuname_entry=ttk.Entry(class_stu_frame,textvariable=self.var_name,width=20,font=("Arial Rounded MT Bold",10,"bold"))
        stuname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label(class_stu_frame,text="Date of join:",font=("Arial Rounded MT Bold",10,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(class_stu_frame,textvariable=self.var_div,width=20,font=("Arial Rounded MT Bold",10,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll No
        rollno_label=Label(class_stu_frame,text="Mobile No:",font=("Arial Rounded MT Bold",10,"bold"),bg="white")
        rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(class_stu_frame,textvariable=self.var_roll,width=20,font=("Arial Rounded MT Bold",10,"bold"))
        rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_stu_frame,text="Gender:",font=("Arial Rounded MT Bold",10,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gen_combo=ttk.Combobox(class_stu_frame,textvariable=self.var_gender,font=("Arial Rounded MT Bold",10,"bold"),state="readonly",width=18)
        gen_combo["values"]=("Select Gender","Male","Female","Other")
        gen_combo.current(0)
        gen_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
        dob_label=Label(class_stu_frame,text="DOB:",font=("Arial Rounded MT Bold",10,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_stu_frame,textvariable=self.var_dob,width=20,font=("Arial Rounded MT Bold",10,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        email_label=Label(class_stu_frame,text="E-mail:",font=("Arial Rounded MT Bold",10,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_stu_frame,textvariable=self.var_email,width=20,font=("Arial Rounded MT Bold",10,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phoneno
        phoneno_label=Label(class_stu_frame,text="Shift_No:",font=("Arial Rounded MT Bold",10,"bold"),bg="white")
        phoneno_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phoneno_entry=ttk.Entry(class_stu_frame,textvariable=self.var_phone,width=20,font=("Arial Rounded MT Bold",10,"bold"))
        phoneno_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        address_label=Label(class_stu_frame,text="Address:",font=("Arial Rounded MT Bold",0,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_stu_frame,textvariable=self.var_add,width=20,font=("Arial Rounded MT Bold",10,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #city
        city_label=Label(class_stu_frame,text="City:",font=("Arial Rounded MT Bold",10,"bold"),bg="white")
        city_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        city_entry=ttk.Entry(class_stu_frame,textvariable=self.var_city,width=20,font=("Arial Rounded MT Bold",10,"bold"))
        city_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radiobutton
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_stu_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=7,column=0)
        radiobtn2=ttk.Radiobutton(class_stu_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=7,column=2)

        #buttonframe

        btn_frame=Frame(class_stu_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=230,width=805,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=13,font=("Arial Rounded MT Bold",15,"bold"),bg="black",fg="#a976e3")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=14,font=("Arial Rounded MT Bold",15,"bold"),bg="black",fg="#a976e3")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=("Arial Rounded MT Bold",15,"bold"),bg="black",fg="#a976e3")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("Arial Rounded MT Bold",15,"bold"),bg="black",fg="#a976e3")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_stu_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=10,y=295,width=805,height=44)

        takephoto_btn=Button(btn_frame1,command=self.generate_dataset,text="Take A Photo Sample",width=60,font=("Arial Rounded MT Bold",15,"bold"),bg="black",fg="#a976e3")
        takephoto_btn.place(x=0,y=0)

        





        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Details",font=("Arial Rounded MT Bold",15,"bold"))
        Right_frame.place(x=930,y=30,width=960,height=650)

        #search system

        

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=25,y=20,width=900,height=600)
        scrollx=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone_no","address","city","photo"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.student_table.xview)
        scrolly.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="EIY")
        self.student_table.heading("year",text="Job Title")
        self.student_table.heading("sem",text="CTC")
        self.student_table.heading("id",text="ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="DOJ")
        
        self.student_table.heading("roll",text="Mobile_No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="E-mail")
        self.student_table.heading("phone_no",text="Shift_No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("city",text="City")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"


        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone_no",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("city",width=100)
        self.student_table.column("photo",width=150)
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #function declearation

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="" or self.var_phone.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("Error","All Feilds are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recognizer")
                my_cursor=conn.cursor()
                #my_cursor.execute("select Student_id from student order by Student_id desc  where rownum<2")
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",( self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_sem.get(),
                                                                                                            self.var_id.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_add.get(),
                                                                                                            self.var_city.get(),
                                                                                                            self.var_radio1.get()))
        
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","Employee details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)    
        

    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_add.set(data[12]),
        self.var_city.set(data[13]),
        self.var_radio1.set(data[14])

    #update fun
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="" or self.var_phone.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("Error","All Feilds are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,email=%s,phone=%s,address=%s,city=%s,photosample=%s where Student_id=%s",(self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_sem.get(),
                                                                                                            
                                                                                                            self.var_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_add.get(),
                                                                                                            self.var_city.get(),
                                                                                                            self.var_radio1.get(),self.var_id.get()))
                else:
                    if  not update:
                        return 
                messagebox.showinfo("Successs","Employee details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #delete function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Employee id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Employee Delete page","Do you want to delete this employee details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted employee details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #reset fun
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_add.set("")
        self.var_city.set("")
        self.var_radio1.set("")


    #generate data set and photo sample
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="" or self.var_phone.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("Error","All Feilds are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                    
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,email=%s,phone=%s,address=%s,city=%s,photosample=%s where Student_id=%s",(self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_sem.get(),
                                                                                                            
                                                                                                            self.var_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_add.get(),
                                                                                                            self.var_city.get(),
                                                                                                            self.var_radio1.get(),self.var_id.get()==id+1))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #load predefined data on face frontal from opencv

                face_classifier=cv2.CascadeClassifier("D:/FDAP/face recognization/haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3,minimum neighbour=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="D:/FDAP/face recognization/data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")
                self.new_window=Toplevel(self.root)
                self.app=Traindata(self.new_window)

                
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                    

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()