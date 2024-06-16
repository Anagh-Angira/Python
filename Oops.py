class Employee:
    salary = 89
    
    name = "Rohan"
    
    def getSalary(self):
        return self.salary

rohan = Employee()
print(rohan.salary) 


class Vehical:
    
    def __init__(self, name, gear):
        
        self.name = name
        self.gear = gear
    
    def getGears(self) :
        return self.gear

audi = Vehical("A4", "6")
print(audi.name)
print(audi.gear)
print(audi.getGears())
         