from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from student import Student
from traindata import Traindata
from face_recognition import Face_recog
from attendance import Attendance



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        self.root.title("Face Recognition System")
        self.root.iconposition(x=0,y=0)
        #self.root.iconbitmap(bitmap=r'1[495].ico')

        #logo img
        
        img=Image.open("D:/FDAP/face recognization/first.png")
        img=img.resize((1950,320),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1950,height=320)

        #bg img
        img1=Image.open("D:/FDAP/face recognization/bgrmain.jpg")
        img1=img1.resize((2000,800),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        s_lbl=Label(self.root,image=self.photoimg1)
        s_lbl.place(x=0,y=300,width=2000,height=770)

        title_lbl=Label(s_lbl,text="Face Recognition Attendance System Software",font=("Arial Rounded MT Bold",35,"bold"),bg="black",fg="#a976e3")
        title_lbl.place(x=0,y=0,width=2000,height=70)

        #student btn
        img2=Image.open("D:/FDAP/face recognization/empicon.png")
        img2=img2.resize((350,290),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(s_lbl,image=self.photoimg2,command=self.student_details,cursor="hand2",bg="black")
        b1.place(x=230,y=100,width=200,height=180)

        b1_1=Button(s_lbl,text="Add Employee",command=self.student_details,cursor="hand2",font=("Arial Rounded MT Bold",12,"bold"),bg="#89a9f0",fg="black")
        b1_1.place(x=230,y=280,width=200,height=40)

        #detect face btn
        img3=Image.open("D:/FDAP/face recognization/face-detection.png")
        img3=img3.resize((200,180),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b2=Button(s_lbl,image=self.photoimg3,cursor="hand2",command=self.face_data)
        b2.place(x=630,y=100,width=200,height=180)

        b2_1=Button(s_lbl,text="Face Detector",cursor="hand2",command=self.face_data,font=("Arial Rounded MT Bold",12,"bold"),bg="#89a9f0",fg="black")
        b2_1.place(x=630,y=280,width=200,height=40)

        #attendance face btn
        img4=Image.open("D:/FDAP/face recognization/attendance (1).png")
        img4=img4.resize((200,180),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b3=Button(s_lbl,image=self.photoimg4,cursor="hand2",command=self.attendance_data,bg="black")
        b3.place(x=1030,y=100,width=200,height=180)

        b3_1=Button(s_lbl,text="Attendance",cursor="hand2",command=self.attendance_data,font=("Arial Rounded MT Bold",12,"bold"),bg="#89a9f0",fg="black")
        b3_1.place(x=1030,y=280,width=200,height=40)

        #train face btn
        img5=Image.open("D:/FDAP/face recognization/train Data.png")
        img5=img5.resize((200,180),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b4=Button(s_lbl,image=self.photoimg5,cursor="hand2",command=self.train_data)
        b4.place(x=1430,y=100,width=200,height=180)

        b4_1=Button(s_lbl,text="Train Data",cursor="hand2",command=self.train_data,font=("Arial Rounded MT Bold",12,"bold"),bg="#89a9f0",fg="black")
        b4_1.place(x=1430,y=280,width=200,height=40)

        #phtos face btn
        img6=Image.open("D:/FDAP/face recognization/photos.png")
        img6=img6.resize((200,180),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b5=Button(s_lbl,image=self.photoimg6,cursor="hand2",command=self.open_img,bg="black")
        b5.place(x=400,y=430,width=200,height=180)

        b5_1=Button(s_lbl,text="Photos",cursor="hand2",command=self.open_img,font=("Arial Rounded MT Bold",12,"bold"),bg="#89a9f0",fg="black")
        b5_1.place(x=400,y=610,width=200,height=40)

        
        


        #exit btn
        img7=Image.open("D:/FDAP/face recognization/exit.png")
        img7=img7.resize((200,180),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b6=Button(s_lbl,image=self.photoimg7,cursor="hand2",command=self.exit,bg="black")
        b6.place(x=1200,y=430,width=200,height=180)

        b6_1=Button(s_lbl,text="Exit",cursor="hand2",command=self.exit,font=("Arial Rounded MT Bold",12,"bold"),bg="#89a9f0",fg="black")
        b6_1.place(x=1200,y=610,width=200,height=40)

        
    def open_img(self):
        os.startfile("D:/FDAP/face recognization/data")    
        
        
        
        
        
        #function buttons

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Traindata(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recog(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()