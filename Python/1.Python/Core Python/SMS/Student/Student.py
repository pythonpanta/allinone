from time import sleep
import sys
class Student:
    def __init__(self,menu):
        self.menu=menu
        self.id=3
        self.student={
            1:{'name':'amrit','address':'banepa'},
            2:{'name':'manita','address':'kathmandu'},
            3:{'name':'pragya','address':'pokhara'},
            }
        print('\n\n\n*********************************************************************************************\n\n')
    def studentMenu(self):
        print('\n\nEnter 1 for Add Student')
        print('Enter 2 for Show All Students Data')
        print('Enter 3 for Show  particular Student Data')
        print('Enter 4 for Update Student')
        print('Enter 5 for Delete Student')
        print('Enter 0 for Logout')
        self.studentchoice=int(input('Enter the option ypu want \n ->'))
        return self.studentchoice
    def studentChoice(self):
        self.choice=self.studentMenu()
        if self.choice==1:
            self.addStudent()
            sleep(2)
        elif self.choice==2:
            self.showStudentDetails()
            sleep(2)
        elif self.choice==3:
            self.searchStudent()
        elif self.choice==4:
            self.editStudent()
        elif self.choice==5:
            self.deleteStudent()
        elif self.choice==0:
            print('Now we are successfully logout from the student ')
            sleep(2)
            self.menu()
    def addStudent(self):
        self.id+=1
        self.name=input('Enter the student name -> ')
        self.address=input('Enter the student address -> ')
        if self.id not in self.student:
            self.student[self.id]={'name':self.name,'address':self.address}
            print(f'\nCongratulation !!! New Student is successfully added \n  your id is {self.id} \n Do remember this ID')
            print('*******************************************************')
            for key,value in self.student.items():
                print(f'ID: {key}')
                for i,val in value.items():
                    print(str(i).title()+':'+str(val).title())
            print('\n*******************************************************')
        else:
            print('\nSorry !! Student cannot be added . Try again')
        sleep(2)
             
    def showStudentDetails(self):
        print('\n\nAll Student Details are as follow \n\n')
        print('*******************************************************')
        for key,value in self.student.items():
            print(f'ID: {key}')
            for i,val in value.items():
                print(str(i).title()+':'+str(val).title())
            print('\n*******************************************************')
        sleep(2)

    def deleteStudent(self):
        self.pk=int(input('\nEnter the Id of student for Delete ->'))
        if self.pk in self.student:
            print('\n*******************************************************')
            self.delete=int(input(f'Are you sure you want to delete {self.pk} ID\n Type 1 for Delete -> '))
            if self.delete==1:
                del self.student[self.pk]
                print(f'Successfully !! Delete the Student with id {self.pk}')
                sleep(2)
            else:
                print('Enter the correct option for deleting the data')
            
            print('\n*******************************************************')
        else:
            print('Sorry this id student is not found in out list')
        sleep(2)
    def editStudent(self):
        self.pk=int(input('\nEnter the Id of student for Edit ->'))
        if self.pk in self.student:
            print('\n*******************************************************')
            self.ename=input('Enter Name for edit')
            self.eaddress=input('Enter Address for edit')
            self.student[self.pk]={'name':self.ename,'address':self.eaddress}
            print('Successfully !! Update the data')
            print(f'ID:{self.pk}')
            for key, value in self.student[self.pk].items():
                print(str(key)+' : '+str(value))
            print('\n*******************************************************')
        else:
            print('Sorry this id student is not found in out list')
        sleep(2)
        
    def searchStudent(self):
        self.pk=int(input('\nEnter the Id of student for search ->'))
        if self.pk in self.student:
            print('\n*******************************************************')
            print(f'ID:{self.pk}')
            for key, value in self.student[self.pk].items():
                print(str(key)+' : '+str(value))
            print('\n*******************************************************')
        else:
            print('Sorry this id student is not found in out list')
        sleep(2)
        
            







