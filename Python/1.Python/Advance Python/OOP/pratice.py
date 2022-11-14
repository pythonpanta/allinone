student={1:'amrit',
        2:'bimal',
        3:'saroj',
        4:'ram'}
# print(student.pop(2))
student.popitem()
for key,value in student.items():
    print(key,value)