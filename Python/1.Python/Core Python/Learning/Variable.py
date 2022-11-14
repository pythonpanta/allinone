'''
In other programming language , varibale can be define as identifier or name , connected to memory location.

What is a variable ?

Variable is a name which is used as a pointer to data that is stored on computer memory.
In python, variables are called as names.
In python variable is consider as a tag that is tied to some value, python consider a value as a object.
In python memeory location is created for the value not for the varibale like C and java language.


message = "Hello World"
print(message)
# Output: Hello World
my_var = "Hi"
print(my_var)
# Output: Hi
print(your_var)
# Output:
# NameError: name 'your_var' is not defined

'''
#lets see some example 
a=10
b=10
name=10
print(id(a)) #id() function is used to see the memory address location for the identifier
print(id(b))
print(id(name))


'''
output:
140712516179904
140712516179904
140712516179904

whose show that all variable 'a','b','c' are tag to the value 10 which is consider as a objevt  in python
'''