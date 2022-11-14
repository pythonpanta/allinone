from fileinput import filename
from sys import path
from tkinter import*
from turtle import width
from PIL import ImageTk, Image, ImageDraw

import numpy as np
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfile 
from tkinter import filedialog as f_d
from tkinter.filedialog import askopenfile

class Tesst:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Train Pannel")

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
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Two",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)


        choose= Button(bg_img,text="Choose Files",command = lambda:self.open_file())
        choose.place(x=600,y=100,width=180,height=45)

        button = Button(root, text="save as", command=self.savefile)
        button.place(x=600,y=500)


        #uploads= Button(bg_img,command=self.uploadFiles,text="Click to Upload the Files",cursor="hand2",font=("tahoma",15,"bold"))
        #uploads.place(x=500,y=350,width=380,height=45)


   #========image Function=======================

    def open_file(self):
        global image_out
        f_types = [('Jpg Files', '*.jpg'),('Jpg Files', '*.jpeg'),('Jpg Files', '*.png')]
        file_name = f_d.askopenfilename(filetypes=f_types)
        image_out = ImageTk.PhotoImage(file=file_name)

        file_name=file_name.name
        b2 =Button(image=image_out) # using Button 
        b2.place(x=130,y=200)
    
    def savefile(self):
        
        fil = f_d.asksaveasfile(mode='wb', defaultextension=".jpg")
        if not filename:
            return
        self.save(filename)

      
if __name__ == "__main__":
    root=Tk()
    obj=Tesst(root)
    root.mainloop()