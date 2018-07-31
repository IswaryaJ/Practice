#Program to make use of Dunder methods
class Employee:
  raise_amt = 2
  
  def __init__(self,name,last,pay):
    self.name = name
    self.last = last
    self.pay = pay

  def fullname(self):
    return ('{}{}'.format(self.name,self.last))
    
  def apply_sal(self):
    self.pay = int(self.pay * self.raise_amt)

  def __len__(self):
    return len(self.fullname())
    
emp_1 = Employee('Ishu', 'Ramesh' , 70000)
emp_2 = Employee('Kiran' ,'Parhad', 70000)

print(len(emp_1))
