from tkinter import*
from PIL import Image,ImageTk
import sys
import subprocess, sys
import os
from student import Student
from train import Train
from take_attend import Take_Attend
from attendance import Attendance



class Dashboard:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1540x790+0+0")
        self.root.title("Face_Recogonition_System")
        self.root.iconbitmap('UI_Images/aa.ico')
 
        img=Image.open(r"UI_Images/banner.jpg")
        img=img.resize((1540,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1540,height=130)

        # backgorund image 
        bg1=Image.open(r"UI_Images/banner.jpg")
        bg1=bg1.resize((1540,768),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1540,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Student Attendance Log Keeping System",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=10,y=100,width=1450,height=50)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"UI_Images/std1.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=100,y=250,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.student_pannels,text="Add Data",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=100,y=420,width=180,height=45)

        # button 2
        det_img_btn=Image.open(r"UI_Images/train2.png")
        det_img_btn=det_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.det_img=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.train_pannels,image=self.det_img,cursor="hand2",)
        det_b1.place(x=330,y=250,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.train_pannels,text="Train Dataset",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=330,y=420,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"UI_Images/rec.png")
        att_img_btn=att_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.att_img=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.face_rec,image=self.att_img,cursor="hand2",)
        att_b1.place(x=580,y=250,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.face_rec,text="Take Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=580,y=420,width=180,height=45)


        # Top 4 buttons end.......
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........
         # Train   button 5
        tra_img_btn=Image.open(r"UI_Images/att1.png")
        tra_img_btn=tra_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.tra_img=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.attendance_pannel,image=self.tra_img,cursor="hand2",)
        tra_b1.place(x=830,y=250,width=180,height=180)

        tra_b1_1 = Button(bg_img,command=self.attendance_pannel,text="View Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        tra_b1_1.place(x=830,y=420,width=180,height=45)


        # exit   button 8
        exi_img_btn=Image.open(r"UI_Images/dataset1.png")
        exi_img_btn=exi_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.exi_img=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.view_dataset,image=self.exi_img,cursor="hand2",)
        exi_b1.place(x=1080,y=250,width=180,height=180)

        exi_b1_1 = Button(bg_img,command=self.view_dataset,text="View Dataset",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        exi_b1_1.place(x=1080,y=420,width=180,height=45)




    

# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Take_Attend(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

  
        
    


    def view_dataset(self):
        os.startfile('dataset')



    def Close(self):
        root.destroy()

    

if __name__ == "__main__":
    root=Tk()
    app=Dashboard(root)
    root.mainloop()
