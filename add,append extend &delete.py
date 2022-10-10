list=[1,2,3]
a=[4,5]
print(" 1.add \n 2.apped \n 3.extend \n 4.delete")
x=int(input("Enter the choice 1/2/3/4 :"))
if x==1:
    list1=list + a
    print(list1)
elif x==2:
    list.append(a)
    print(list)
elif x==3:
    list.extend(a)
    print(list)
elif x==4:
    list.remove(1)
    print(list)
else:
    print("invalid input")
