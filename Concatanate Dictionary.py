#Concatanate 3 dictionaries
dict1={292:'Heet',295:'Hemil',297:'Atri'}
dict2={101:'Het',102:'Rachana',103:'Gaurav'}
dict3={201:'Shreya',202:'Ojas',203:'Chandrayan'}
dict4={}

print('Dictionary 1:',dict1)
print('Dictionary 2:',dict2)
print('Dictionary 3:',dict3)

#Method 1:
dict4.update(dict1)
dict4.update(dict2)
dict4.update(dict3)
print('Concatanation Successful!')
print('New Dictionary =',dict4)

#Method 2:
combined={**dict1,**dict2,**dict3}
print('Concatanation Successful')
print('New Dictionary =',combined)





