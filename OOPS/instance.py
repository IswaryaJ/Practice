class Employee:
  def __init__(self,name,last,age):
    self.name = name
    self.last = last
    self.age = age
    
  def fullname(self):
    return ('{}{}'.format(self.name,self.last))


emp1 = Employee('Ishu', 'Ramesh', '25')
emp2 = Employee('Kiran','Parhad','26')


print(emp1.fullname())
print(Employee.fullname(emp2))

print(emp1.name)
print(emp2.name)
