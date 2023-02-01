from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]

class Attendance:
    def __init__(self,root):
        self.root=root
        
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        self.root.title("Face Recognition System")
        self.root.iconposition(x=0,y=0)
        #self.root.iconbitmap(bitmap=r'1[495].ico')


        #variable
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        
        img=Image.open("D:/FDAP/face recognization/first.png")
        img=img.resize((1950,420),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1950,height=420)


        title_lbl=Label(self.root,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="purple")
        title_lbl.place(x=0,y=350,width=2000,height=50)

        #left label frame
        Left_frame=LabelFrame(self.root,bd=2,bg="white",relief=RIDGE,text="Students Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=5,y=390,width=950,height=650)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=10,y=5,width=925,height=600)

        #labels and entries

        #attendance id
        att_id_label=Label(left_inside_frame,text="AttendanceID :",font=("times new roman",15,"bold"),bg="white")
        att_id_label.place(x=25,y=40,width=150,height=25)

        attID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attID_entry.place(x=190,y=40,width=150,height=25)

        #Name
        name_label=Label(left_inside_frame,text="Name :",font=("times new roman",15,"bold"),bg="white")
        name_label.place(x=460,y=40,width=150,height=25)

        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        name_entry.place(x=605,y=40,width=150,height=25)

        #Roll
        roll_label=Label(left_inside_frame,text="Shift_No :",font=("times new roman",15,"bold"),bg="white")
        roll_label.place(x=25,y=140,width=150,height=25)

        roll_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        roll_entry.place(x=190,y=140,width=150,height=25)

        #Department
        dep_label=Label(left_inside_frame,text="Department :",font=("times new roman",15,"bold"),bg="white")
        dep_label.place(x=460,y=140,width=150,height=25)

        dep_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        dep_entry.place(x=605,y=140,width=150,height=25)

        #time
        time_label=Label(left_inside_frame,text="Time :",font=("times new roman",15,"bold"),bg="white")
        time_label.place(x=25,y=240,width=150,height=25)

        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        time_entry.place(x=190,y=240,width=150,height=25)

        #date
        date_label=Label(left_inside_frame,text="Date :",font=("times new roman",15,"bold"),bg="white")
        date_label.place(x=460,y=240,width=150,height=25)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        date_entry.place(x=605,y=240,width=150,height=25)

        

        #Attendance status
        atst_label=Label(left_inside_frame,text="Attendance Status :",font=("times new roman",15,"bold"),bg="white")
        atst_label.place(x=0,y=340,width=190,height=25)

        atst_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly",width=18)
        atst_combo["values"]=("Status","Present","Absent")
        atst_combo.current(0)
        atst_combo.place(x=190,y=340,width=150,height=25)

        #buttonframe

        btn_frame=Frame(left_inside_frame,bd=0,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=450,width=910,height=45)

        save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=20,font=("times new roman",15,"bold"),bg="#f54b38",fg="white")
        save_btn.place(x=20,y=0)

        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=20,font=("times new roman",15,"bold"),bg="#8aed77",fg="white")
        update_btn.place(x=340,y=0)

        

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=20,font=("times new roman",15,"bold"),bg="#89a9f0",fg="white")
        reset_btn.place(x=670,y=0)


       


        #right label frame
        Right_frame=LabelFrame(self.root,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=960,y=390,width=950,height=650)

        tbl_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        tbl_frame.place(x=10,y=5,width=925,height=610)

        #scrollbar  table

        scroll_x=ttk.Scrollbar(tbl_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tbl_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(tbl_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Shift_No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #fetch data
    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Empty","No Data Found To Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported","Your Data Is Exported to "+os.path.basename(fln)+"Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)   

    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    #reset_date
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("") 
        self.var_atten_roll.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        









if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()