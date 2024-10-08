yr=int(input("enter the year"))
for i in range(yr,2025):
    if(i%4==0)and(i%100!=0) or(i%400==0):
        print(i,"leap year")
    else:
        print(i,"not leap year")
      
