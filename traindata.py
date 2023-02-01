from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np





class Traindata:
    def __init__(self,root):
        self.root=root
        
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        self.root.title("Face Recognition System")
        self.root.iconposition(x=0,y=0)
        #self.root.iconbitmap(bitmap=r'1[495].ico')


      
        img=Image.open("D:/FDAP/face recognization/first.png")
        img=img.resize((1950,320),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1950,height=320)

        

        
        #button

        b1_1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",40,"bold"),bg="black",fg="white")
        b1_1.place(x=0,y=300,width=1912,height=60)


        img_bottom=Image.open("D:/FDAP/face recognization/traintop1.jpg")
        img_bottom=img_bottom.resize((635,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        s_lbl3=Label(self.root,image=self.photoimg_bottom)
        s_lbl3.place(x=0,y=360,width=635,height=700)

        img_bottom1=Image.open("D:/FDAP/face recognization/trainbottom3.png")
        img_bottom1=img_bottom1.resize((635,700),Image.ANTIALIAS)
        self.photoimg_bottom1=ImageTk.PhotoImage(img_bottom1)

        s_lbl4=Label(self.root,image=self.photoimg_bottom1)
        s_lbl4.place(x=635,y=360,width=635,height=700)

        img_bottom2=Image.open("D:/FDAP/face recognization/traintop2.png")
        img_bottom2=img_bottom2.resize((642,700),Image.ANTIALIAS)
        self.photoimg_bottom2=ImageTk.PhotoImage(img_bottom2)

        s_lbl4=Label(self.root,image=self.photoimg_bottom2)
        s_lbl4.place(x=1270,y=360,width=642,height=700)

    def train_classifier(self):
        data_dir=("D:/FDAP/face recognization/data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale img
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("D:/FDAP/face recognization/classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Data Set Finish")

                    
        
        
        
        

        








if __name__ == "__main__":
    root=Tk()
    obj=Traindata(root)
    root.mainloop()