st={}
st["name"]=input("enter the name")
st["roll no"]=int(input("enter the roll no"))
st["deapartment"]=input("enter the department")
st["semester"]=int(input("enter the semester"))

print("the details before total mark", st)

st["total_mark"] =int(input("enter the total mark"))
print("the details after total mark", st)
print( )


total=st["total_mark"]
if total>=90:
    st["grade"]="A"
elif total>=82:
    st["grade"]="B"
elif total>=75:
    st["grade"]="c"
elif total>=60:
    st["grade"]="D"
elif total>=50:
    st["grade"]="P"

print()   
print("with update grade", st)

del st["roll no"]
print("after the roll number key delete",st)
print()   
