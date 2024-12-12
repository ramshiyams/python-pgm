class employee:
    def__init__(self,name,salary):
        #public member
        self.name=name
        #private
        self.__salary=salary
   def show(self):
       print("name is",self.name,"salary is",self.__salary)
emp=employee("jessa",4000)
emp.show()
print(emp.name)
    
