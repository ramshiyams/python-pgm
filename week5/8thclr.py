li=[]
l2=[]
s=int(input("enter the size of list"))
for i in range(0,s):
    st=input("enter the clr")
    li.append(st)
print(li)
l2.append(li[0])
l2.append(li[-1])
print(l2)
