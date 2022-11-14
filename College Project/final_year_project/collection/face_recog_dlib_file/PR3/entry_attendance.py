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


class Entry_Attendance:
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

     # Entry button 2

        std_img_btn=Image.open(r"UI_Images/verify.png")
        std_img_btn=std_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.std_img2=ImageTk.PhotoImage(std_img_btn)

        std_b2 = Button(bg_img,command=self.entry,image=self.std_img2,cursor="hand2")
        std_b2.place(x=600,y=170,width=180,height=180)

        std_b1_2 = Button(bg_img,command=self.entry,text="Mark Entry Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_2.place(x=600,y=350,width=180,height=45)



#===========================Atttendance=======================
    def entry(self):
        def Final_csv(file_name):
            f = pd.read_csv(file_name)
            f = f.drop_duplicates(subset=['Name'])
            f.to_csv(file_name, index=False)

        def findEncodings(images):
            encodeList = []

            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                encodeList.append(encode)
            return encodeList

        def markTIMEentry(name, Win_name):
            print("marking entry")
            Win_name += '.csv'
            with open(Win_name, 'r+') as f:
                myDataList = f.readlines()

                for line in myDataList:
                    entry = line.split(',')
                    nameList.append(entry[0])
                    if name not in nameList:
                        now = datetime.now()
                        dtString = now.strftime('%H:%M:%S')
                        f.writelines(f'\n{name},{dtString}')

        def cameraENTRY(img, Win_name):
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    markTIMEentry(name, "ENTRY")
                else:
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img,"unknown", (x1 + +6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    

            cv2.imshow(Win_name, img)

        path = 'Training_images'

        images = []
        classNames = []
        myList = os.listdir(path)
        print("my list", myList)

        for cl in myList:
            curImg = cv2.imread(f'{path}/{cl}')
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])
        print("classnames", classNames)
        print("images", images)
        nameList = []

        encodeListKnown = findEncodings(images)
        print('Encoding Complete')

        cap = cv2.VideoCapture(0)

        while True:
            success, img = cap.read()

            cameraENTRY(img, 'ENTRY')
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        print("calling final csv")
        Final_csv("ENTRY.csv")

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=Entry_Attendance(root)
    root.mainloop()


    