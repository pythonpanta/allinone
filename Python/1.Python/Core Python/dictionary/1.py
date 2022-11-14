# syntax: dic_name={}
# example 

'''

my_dict={1:'amrit',2:'ram',3:'shyam'}
del my_dict[3]
print(1 in my_dict)
print(5 in my_dict)


'''
# fromkeys()
# key=(1,2,3,4,5)
# values='amrit panta'
# new_dict=dict.fromkeys(key,values)
# print(new_dict)



# my_dict={1:'amrit',2:'ram',3:'shyam'}
# print(my_dict.keys())


# getting data from the usser in t edictionary 
a={}
n=int(input('how many data do you want to enter in dictionary ->'))
for i in range(n):
    id=input('enter id -> ')
    data=input('enter name -> ')
    a.update({id:data})

print('your new dictionary would look like ')
for i in a:
    print(i,':',a[i])
