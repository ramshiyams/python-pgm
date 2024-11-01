str=input("enter the string")
if(str[-3:]=='ing'):
   str=str[:-3]+'ly'
else:
    str=str=str+"ing"
print(str)
