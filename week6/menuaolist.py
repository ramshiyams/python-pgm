l1=[4,2,5,66,34]
print(l1)
srt=[]
evelist=[]
while True:
    print("1.find the greates and lowset number")
    print("2.sort list(asc) ")
    print("3.list of even number")
    choice=int(input("enter the option"))
    print()
    if choice==1:
        print("largest number",max(l1))
        print("lowest number",min(l1))
        print()
    elif choice==2:
        l1.sort()
        print("sorted list is",l1)
        print()
    elif choice==3:
        for i in l1:
            if i%2==0:
                evelist.append(i)
        print("even number list",evelist,)
    
