# def add(a,b):
#     '''this is the function to add two number'''
#     print(a+b)
# add(5,6)
# print(add.__doc__)


'''
a=True if 50>6 else False
print(a)


'''
'''
import os
path=os.getcwd()
for i in range(5):
    os.mkdir(path+f'\\{i}')
'''
# import os
# os.mkdir('amrit')


data={
    'username':'amrit',
    'password':'123nepal'
}
if 'usernames' in data:
    print('yes')
else:
    print('no')