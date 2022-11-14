from Student.Student import Student
import time
import sys
def menu():
    print('Enter 1 For Student')
    print('Enter 2 For Teacher')
    print('Enter 3 For Admin')
    print('Enter 4 For Library')
    print('Enter 0 For Exit')
    choice=int(input('Enter the option  you want \n ->'))
    return choice

def makeChoice():
    c=menu()
    if c==1:
        s=Student(makeChoice)
        while 1:
            s.studentChoice()
        
    elif c==2:
        print('This is teacher panel')
    elif c==3:
        print('This is Admin panel')
    elif c==4:
        print('This is admin panel')
    elif c==0:
        print('\nNow you are successfully logout. Thank you . Hope to see you soon')
        time.sleep(2)
        sys.exit(0)
    else:
        print('\nPlease Enter the correct option mention above')
        time.sleep(2)
    


# startinf point of program 
print('\n\n**********************************************************************************\n')
print('Welcome to School Management system')
while 1:
    makeChoice()
