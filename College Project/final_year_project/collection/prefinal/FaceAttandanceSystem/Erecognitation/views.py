from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import usernameForm
import os
import cv2
import numpy as np

def username_present(username):
	if User.objects.filter(username=username).exists():
		return True
	return False

def create_dataset(id):
    try:
        face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        def face_croped(img):
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=face_classifier.detectMultiScale(gray,1.3,5)
            for(x,y,w,h) in faces:
                face_cropped=img[y:y+h,x:x+w]
                return face_cropped
        cap=cv2.VideoCapture(0)
        imag_id=0
        while True:
            ret,myframe=cap.read()
            if face_croped(myframe) is not None:
                imag_id+=1
                face=cv2.resize(face_croped(myframe),(450,450))
                face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                filename_path='data/user.'+str(id)+'.'+str(imag_id)+'.jpg'
                cv2.imwrite(filename_path,face)
                cv2.putText(face,str(imag_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                cv2.imshow('Cropped image',face)
                cv2.waitKey(10)
            if int(imag_id)==100:
                break
        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(e)
    



    

def Home(request):
    return render(request,'Erecognitation/home.html')


@login_required
def DashBoard(request):
    if request.user.username=='admin':
        total=User.objects.all().count()
        total-=1 #as one is the admin 
        return render(request,'Erecognitation/admindashboard.html',{'total':total})
    else:
        user=request.user.username
        return render(request,'Erecognitation/userdashboard.html',{'user':user})


def Attandance_IN(request):
    def draw_boundary(img,classifier,scalefactor,minneighbors,color,text,clf):
        gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        features=classifier.detectMultiScale(gray_image,scalefactor,minneighbors)
        coord=[]
        for(x,y,w,h) in features:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
            id,predict=clf.predict(gray_image[y:y+h,x:x+w])
            euser=User.objects.filter(pk=id)
            for e in euser:
                username=e
            confidence=int((100*(1-predict/300)))

            if confidence>77:
                cv2.putText(img,f'Roll:  {id}',(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(10, 223, 242),3)
                cv2.putText(img,f'Username:  {username}',(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(10, 223, 242),3)
            else:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                cv2.putText(img,'Unknow face',(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
            coord=[x,y,w,h]
        return coord

    def recognize(img,clf,faceCascade):
        coord=draw_boundary(img,faceCascade,1.1,10,(255,255,155),'Face',clf)
        return img


    faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    clf=cv2.face.LBPHFaceRecognizer_create()
    clf.read('classifier.xml')
    
    video_cap=cv2.VideoCapture(0)

    while True:
        ret,img=video_cap.read()
        img=recognize(img,clf,faceCascade)
        cv2.imshow('Welcome to Face Recognization',img)

        # if cv2.waitKey(1)==13:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_cap.release()
    cv2.destroyAllWindows()
    return render(request,'Erecognitation/attandance_in.html')

def Attandance_OUT(request):
    return render(request,'Erecognitation/attandance_out.html')


@login_required
def View_Attendance(request):
    return render(request,'Erecognitation/view_attendance.html')


@login_required
def Trainsystem(request):
    data_dir=('data')
    path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
    faces=[]
    ids=[]
    for image in path:
        image1 = cv2.imread(image)
        gray=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
        imageNp=np.array(gray,'uint8')
        pk=int(os.path.split(image)[1].split('.')[1])
        faces.append(imageNp)
        ids.append(pk)
        cv2.imshow('Training',imageNp)
        cv2.waitKey(1)
    ids=np.array(ids)
    # train classifier 
    clf=cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces,ids)
    clf.write('classifier.xml')
    cv2.destroyAllWindows()
    messages.success(request,'Training data set completed')
    return render(request,'Erecognitation/trainsystem.html')



@login_required
def Addphoto(request):
    if request.method=='POST':
        data=request.POST.copy()
        username=data.get('username')
        if username_present(username):
            user=User.objects.get(username=username)
            id=user.pk
            create_dataset(id)
            messages.success(request, f'Dataset Created')
            return render(request,'Erecognitation/addphoto.html')
            # return redirect('Addphoto')
            
        else:
            messages.warning(request, f'No such username found. Please register employee first.')
            return redirect('Addphoto')
    else:
        form=usernameForm()
        return render(request,'Erecognitation/addphoto.html', {'form' : form})




@login_required
def Viewreport(request):
    return render(request,'Erecognitation/viewreport.html')
   


