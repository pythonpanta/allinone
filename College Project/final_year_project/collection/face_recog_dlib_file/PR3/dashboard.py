from dataclasses import dataclass
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter as tk
import numpy as np
import os
import sys
import subprocess, sys
from entry_attendance import Entry_Attendance
from exit_attendance import Exit_Attendance

from student import Student
from entry_attendance import Entry_Attendance
from train import Train
from take_attend import Take_Attend
from attendance import Attendance
from Face_Loc import Face_Locator


class Dashboard:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"UI_Images/banner.jpg")
        img=img.resize((1366,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"UI_Images/banner.jpg")
        bg1=bg1.resize((1366,768),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=50,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="ⓢ Student Attendance Log Keeping Using LBPH",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=50)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"UI_Images/std1.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=100,y=100,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.student_pannels,text="Add Data",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=100,y=280,width=180,height=45)

        # button 2
        det_img_btn=Image.open(r"UI_Images/train2.png")
        det_img_btn=det_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.det_img=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.train_pannels,image=self.det_img,cursor="hand2",)
        det_b1.place(x=330,y=100,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.train_pannels,text="Train Dataset",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=330,y=280,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"UI_Images/rec.png")
        att_img_btn=att_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.att_img=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.face_rec,image=self.att_img,cursor="hand2",)
        att_b1.place(x=580,y=100,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.face_rec,text="Take Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=580,y=280,width=180,height=45)


        # Top 4 buttons end.......
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........
         # Train   button 5
        tra_img_btn=Image.open(r"UI_Images/att1.png")
        tra_img_btn=tra_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.tra_img=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.attendance_pannel,image=self.tra_img,cursor="hand2",)
        tra_b1.place(x=830,y=100,width=180,height=180)

        tra_b1_1 = Button(bg_img,command=self.attendance_pannel,text="View Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        tra_b1_1.place(x=830,y=280,width=180,height=45)


        # exit   button 8
        exi_img_btn=Image.open(r"UI_Images/dataset1.png")
        exi_img_btn=exi_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.exi_img=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.view_dataset,image=self.exi_img,cursor="hand2",)
        exi_b1.place(x=1080,y=100,width=180,height=180)

        exi_b1_1 = Button(bg_img,command=self.view_dataset,text="View Dataset",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        exi_b1_1.place(x=1080,y=280,width=180,height=45)


     #title section
        title_lb2 = Label(bg_img,text="ⓢ Student Attendance Log Keeping Using face_recognition() System",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb2.place(x=40,y=340,width=1366,height=45)

    

    
    #Section 2===================

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn2=Image.open(r"UI_Images/enr.png")
        std_img_btn2=std_img_btn2.resize((180,180),Image.Resampling.LANCZOS)
        self.std_img2=ImageTk.PhotoImage(std_img_btn2)

        std_b2 = Button(bg_img,command=self.face_loc_dataset,image=self.std_img2,cursor="hand2")
        std_b2.place(x=100,y=400,width=180,height=180)

        std_b1_2 = Button(bg_img,command=self.face_loc_dataset,text="Start Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_2.place(x=100,y=580,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"UI_Images/att.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.mark_entry,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=330,y=400,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.mark_entry,text="Mark Entry Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=330,y=580,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"UI_Images/det1.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.mark_exit,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=580,y=400,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.mark_exit,text="Mark Exit Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=580,y=580,width=180,height=45)


        # Top 4 buttons end.......
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........
         # Train   button 5
        tra_img_btn=Image.open(r"UI_Images/view_record.jpg")
        tra_img_btn=tra_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.attendance_pannel,image=self.tra_img1,cursor="hand2",)
        tra_b1.place(x=830,y=400,width=180,height=180)

        tra_b1_1 = Button(bg_img,command=self.attendance_pannel,text="View Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        tra_b1_1.place(x=830,y=580,width=180,height=45)


        # exit   button 8
        exi_img_btn=Image.open(r"UI_Images/dataset2.png")
        exi_img_btn=exi_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.view_dataset2,image=self.exi_img1,cursor="hand2",)
        exi_b1.place(x=1080,y=400,width=180,height=180)

        exi_b1_1 = Button(bg_img,command=self.view_dataset2,text="Dataset",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        exi_b1_1.place(x=1080,y=580,width=180,height=45)



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

    
    def face_loc_dataset(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Locator(self.new_window)
        
    
    def mark_entry(self):
        self.new_window=Toplevel(self.root)
        self.app=Entry_Attendance(self.new_window)
    
    def mark_exit(self):
        self.new_window=Toplevel(self.root)
        self.app=Exit_Attendance(self.new_window)

    def view_dataset(self):
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, 'dataset'])

    def view_dataset2(self):
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, 'Training_images'])


    def Close(self):
        root.destroy()

    

if __name__ == "__main__":
    root=Tk()
    app=Dashboard(root)
    root.mainloop()
