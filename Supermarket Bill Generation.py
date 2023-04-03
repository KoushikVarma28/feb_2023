from datetime import datetime

Name=input("Enter your name: ")
#List of items
lists='''
Rice Rs 20/kg
Sugar Rs 30/kg
Oil   RS 40/kg
Maggie Rs 50/kg
'''

price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

items={'rice':20,
'sugar':30,
'oil':40,
'maggie':50}
option=int(input("for list of items press 1: "))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit: "))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items: ")
        quantity=int(input("Enter quantity: "))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no: ")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","Koushik supermarket",25*"=")
            print(28*" ","Vijayawada")
            print("Name: ",Name,30*" ","Date: ",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,6*' ',3*' ',ilist[i],7*' ',qlist[i],10*" ",plist[i])  
            print(75*"-")
            print(50*" ",'TotalAmount: ','Rs',totalprice)    
            print("gst amount",52*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalAmount: ','Rs',finalamount) 
            print(75*"-")
            print(25*" ","Thanks You,Visit Again")
            print(75*"-")

                 
                       

