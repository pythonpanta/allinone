# nesting dictionary 
new_dictionary={
   'name':'amrit',
   'roll':1,
   'skills':{1:'python',2:'react',3:'django'}
}
for i in new_dictionary:
    if type(new_dictionary[i]) is dict:
        for k in new_dictionary[i]:
            print(k,':',new_dictionary[i][k])
    else:
        print(i,':',new_dictionary[i]) 
