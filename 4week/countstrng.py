strng=input("enter text:")
word=input("enter the word")
a=[]
count=0
a=strng.split(" ")
for i in range(0,len(a)):
    if (word==a[i]):
        count=count+1
print("count of the word is :",count)
