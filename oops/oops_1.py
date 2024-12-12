class Employee:
    basic=0
    ta=0
    da=0
    def salary(self):
        print("salary ",self.basic+self.ta+self.da)
empl=Employee()
empl.basic=2000
empl.ta=8900
empl.da=5008
empl.salary()
