#Program to make use of class method
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
    
  @classmethod
  def set_raise(cls,amt):
    cls.raise_amt = amt
    
  @classmethod
  def new_str(cls,emp_str):
    first,last,pay = emp_str.split('-')
    return cls(first,last,pay)
    

emp1 = Employee('Ishu', 'Ramesh', '70000')

print(emp1.raise_amt)
Employee.set_raise(4)
print(emp1.raise_amt)

new_emp1 = 'Bunty-Humpty-80000'
new_emp2 = 'Tom-Jerry-90000'

new_emp = Employee.new_str(new_emp2)
print(new_emp.name)


