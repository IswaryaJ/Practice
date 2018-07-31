#Program to make use of class variable
class Employee:
  raise_amt = 2
  
  No_Emp = 0
  
  def __init__(self,name,last,pay):
    self.name = name
    self.last = last
    self.pay = pay
    
    Employee.No_Emp += 1
  def fullname(self):
    return ('{}{}'.format(self.name,self.last))
    
  def apply_sal(self):
    self.pay = int(self.pay * self.raise_amt)
    

emp1 = Employee('Ishu', 'Ramesh', '70000')

print(emp1.pay)
emp1.apply_sal()
print(emp1.pay)
print(Employee.No_Emp)
