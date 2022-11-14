from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfile 
import time
from tkinter .ttk import Progressbar
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

class Two:
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

        #uploads= Button(bg_img,command=self.uploadFiles,text="Click to Upload the Files",cursor="hand2",font=("tahoma",15,"bold"))
        #uploads.place(x=500,y=350,width=380,height=45)

    
   #========image Function=======================

    def open_file(self):
        global img
        f_types = [('Jpg Files', '*.jpg'),('Jpg Files', '*.jpeg'),('Jpg Files', '*.png')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        img = ImageTk.PhotoImage(file=filename)
        b2 =Button(root,image=img) # using Button 
        b2.place(x=130,y=200)
       

      
if __name__ == "__main__":
    root=Tk()
    obj=Two(root)
    root.mainloop()