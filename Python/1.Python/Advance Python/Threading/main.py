# import threading

'''
main thread is the the thread which is rrun by the PVM when we run the python program
'''
# t=threading.current_thread().getName()
# t=threading.current_thread().getName()
# print(t)

'''
creating the thread can be 3 types
1.creating the thread without using the class
2.creating the thread by using the child class for the THREAD class
3.creating the thread without creating child class to the=rea class
'''
#   1.creating the thread without using a class 
from threading import Thread
def myfun(a,b):
    print(a,b)
t1=Thread(target=myfun,args=(2,6))
t1.start()
