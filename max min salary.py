#Max min salary
import operator
emp_data={(1,'#100'):20000,(2,'#101'):25000,(1,'#201'):26750,(2,'#401'):40000}
dept_data={}

for key,value in emp_data.items():
    print(key[0],key[1],value)
for key in emp_data:
    if key[0] not in dept_data:
        dept_data[key[0]]={'max':emp_data[key],'min':emp_data[key],'total':0}
    if emp_data[key]<dept_data[key[0]]['min']:
        dept_data[key[0]]['min']=emp_data[key]
    if emp_data[key]>dept_data[key[0]]['max']:
        dept_data[key[0]]['max']=emp_data[key]
    dept_data[key[0]]['total']+=emp_data[key]
print(dept_data)
                  


