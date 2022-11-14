'''
python calss is the group of the attributes and  methods.
attributes=represents by variables that ccontains data
method=it performs actions or tasks . it is similar to the functions


objects is class type variables or class instance
to use the class we sdhuld create the object of the class


instance creations or object creation represent the allocating memory necessary to store actual data of the variables.'
each time you create the object of the calss, a copy of each variable of calss is created
'''
class Student:
    def lend_book(self):
        name=input('enter your name -> ')
        book=input('Enter book to be lend -> ')
    def took_book(self):
        pass





class Library:
    def __init__(self,name):
        self.name=name
        self.books={1:'Nepali',2:'English',3:'Social',4:'Science'}
        print(f'Welcome To {self.name} Library')
        
    def show_book(self):
        if self.books:
            print('Available book in Library are: ')
            print('ID: Name')
            for key,value in self.books.items():
                print(key,':',value)
        else:
            print('No book in Library at the moment')
    def add_book(self):
        book_id=int(input('Enter Book id zto be added - > '))
        book_name=input('Enter Book id zto be added - > ')
        self.books.update({book_id:book_name})

# object creations 
obj=Library('ABC')
obj.show_book()
obj.add_book()
obj.show_book()