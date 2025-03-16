#grocery Bill
'''
import operator
gro_price={'milk':150,'cheese':300,'butter':120}
gro_quantity={'milk':3,'cheese':2,'butter':0}

total=0

bill={}
for k,v in gro_price.items():
    if k in gro_quantity:
        bill[k]=v*gro_quantity[k]
        total+=v*gro_quantity[k]
        
sorted_bill=dict(sorted(bill.items(),key=operator.itemgetter(1)))
print(bill)
print(sorted_bill)
print('total Bill:',total)
'''
import operator
gro_price={'milk':150,'cheese':300,'butter':120}
gro_quantity={(1,'milk'):3,(1,'cheese'):2,(2,'butter'):1}

total=0

bill={}
for k,v in gro_quantity.items():
    if k[1] in gro_price:
        if k[0] not in bill:
            bill[k[0]]=0
        bill[k[0]]+=v*gro_price[k[1]]
        
print(bill)

