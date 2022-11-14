from sys import path
from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk
import os
import numpy as np
from tkinter import *
from PIL import ImageTk, Image
import face_recognition
from datetime import *
import pandas as pd
import cv2


class Face_Locator:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Train Pannel")
      

        #===========backgrounnd image=============
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
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Training Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Buttons
        std_img_btn2=Image.open(r"UI_Images/add.png")
        std_img_btn2=std_img_btn2.resize((180,180),Image.Resampling.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn2)

        std_b1 = Button(bg_img,command=self.update1,image=self.std_img1,cursor="hand2")
        std_b1.place(x=400,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.update1,text="Create Dataset",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=400,y=350,width=180,height=45)



    def update1(self):
        path = 'Training_images'
        e = ''
        def setname():
            ret, frame = cap.read()
            name = e.get()
            name = name + ".png"
            cv2.imwrite(os.path.join(path, name), frame)

    
        # Create a frame
        window=Toplevel(self.root)
        app = Frame(window, bg="white")
        app.grid()

        # Create a label in the frame
        lmain = Label(app)
        lmain.grid()

        # Capture from camera
        cap = cv2.VideoCapture(0)

        # function for video streaming
        def video_stream():
            _, frame = cap.read()
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            lmain.after(1, video_stream)

        e = Entry(window, width=20, font=('Times 15'))
        e.place(x=550, y=600, width=220, height=25)
        e.focus_set()

        b = Button(window, text='UPDATE', command=setname, width=20, font=('Helvetica 15'), bg="white", fg="black")
        b.place(x=550, y=650, width=220, height=50)
        video_stream()
        window.mainloop()
        cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root=Tk()
    obj=Face_Locator(root)
    root.mainloop()


    