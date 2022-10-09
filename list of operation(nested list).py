print(" 1:Nested list \n 2.lenght \n 3.concatenation \n 4.membership \n 5.indexing \n 6.slicing")
x=int(input("Enter the choice to perform from above operations"))
if x==1:
    Nested_List = [10, 20, 30,['a', 'b', 'c'], 50]
    Sub_List = Nested_List[3] 
    data = Nested_List[3][1]
    print("List inside the nested list: ", Sub_List)
    print("Second element of the sublist: ", data)
elif x==2:
    list=[10,20,30,40,50,60]
    l=len(list)
    print(l)
elif x==3:
    a="maaruboina"
    b="dileep"
    c=a+b
    print(c)
elif x==4:
    a=[1,2,3,4,5,6]
    p= 2 in a
    q= 4 not in a
    r= 10 in a
    print("p statement is:",p)
    print("q statement is:",q)
    print("r statement is:",r)
elif x==5:
    l=[5,10,15,20,25]
    print("indexing 1st element",l[0])
    print("indexing 3rd element",l[2])
elif x==6:
    a=[10,20,30,40,50]
    print("first four elements are:",a[0:3])
    print("last element is:",a[-1])
else:
    print("Invalid input")
