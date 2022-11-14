from tkinter import*
from PIL import Image,ImageTk
import time
from tkinter .ttk import Progressbar
from login import Login
class Splash_Screen:
    def __init__(self,root):
        self.root=root
        self.root.title("Welcome.......")
        self.root.geometry("1540x790+0+0")
        self.root.iconbitmap('images/aa.ico')


        # backgorund image 
        bg1=Image.open(r"UI_Images/five.jpeg")
        bg1=bg1.resize((1540,790),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

   

        self.bg=ImageTk.PhotoImage(file=r"UI_Images/login_bg.jpg")

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1540,height=790)


        #title section
        title_lb1 = Label(bg_img,text="Student Attendance  Using Face Recognition System",font=("verdana",30,"bold"),bg="#e28447",fg="white")
        title_lb1.place(x=0,y=0,width=1540,height=85)

        
        pb1 = Progressbar(root,orient=HORIZONTAL,length=1100,mode='determinate')
        pb1.pack(pady=10)
        pb1.place(x=200,y=650)
        pb1.start

        for i in range(5):
            root.update_idletasks()
            pb1['value'] += 20
            time.sleep(1)
        pb1.destroy()
        win=root
        Login(win)


    
if __name__ == "__main__":
    root=Tk()
    app=Splash_Screen(root)
    root.mainloop()