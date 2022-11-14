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



class Take_Attendance:
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
        # Take Attendance

        std_img_btn=Image.open(r"UI_Images/att.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b2 = Button(bg_img,command=self.attendance,image=self.std_img1,cursor="hand2")
        std_b2.place(x=500,y=170,width=180,height=180)

        std_b1_2 = Button(bg_img,command=self.attendance,text="Take Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_2.place(x=500,y=350,width=180,height=45)


#===========================Atttendance=======================
    def attendance(self):
        def clear_CSV(file_name):
            file = open(file_name, "r+")
            file.truncate(16)
            file.close()

        def TOminutes(Entry, Exit):
            IN = Entry.split(':')
            OUT = Exit.split(':')
            t1 = (int)(IN[0]) * 60 + (int)(IN[1])
            t2 = (int)(OUT[0]) * 60 + (int)(OUT[1])
            return t2 - t1

        df1 = pd.read_csv("ENTRY.csv")
        df2 = pd.read_csv("EXIT.csv")
        LIST = pd.read_csv("LIST.csv")

        result = df1.merge(df2, indicator=True, how='outer').loc[lambda v: v['_merge'] == 'both']
        result.drop(['_merge'], axis=1, inplace=True)

        result['DURATION'] = 0

        for i in range(result.shape[0]):
            result['DURATION'][i] = TOminutes(result['Time_ENTRY'][i], result['Time_EXIT_'][i])

        # dropping student records who have a duration less than a specified threshold
        result = result.drop(result[result.DURATION < 1].index)

        for i in range(LIST.shape[0]):
            if result.shape[0] != 0:
                for j in range(result.shape[0]):
                    if result['Name'][j] == LIST['Name'][i]:
                        LIST['ATTENDANCE'][i] = "PRESENT"
                    else:
                        LIST['ATTENDANCE'][i] = "ABSENT"
            else:
                LIST['ATTENDANCE'][i] = "ABSENT"

        
        print(df1)
        print()
        print(df2) 
        print()
        print(result)            
        print() 
    

        t = date.today()

        t = t.strftime("%m-%d-%Y")
        t = t + '.csv'

        print(LIST)

        LIST.to_csv(t)

        clear_CSV("ENTRY.csv")
        clear_CSV("EXIT.csv")

if __name__ == "__main__":
    root=Tk()
    obj=Take_Attendance(root)
    root.mainloop()


    