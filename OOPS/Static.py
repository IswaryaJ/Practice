#Program to make use of static method
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
    
  @staticmethod
  def is_workday(day):
    if day.weekday == 5 or day.weekday == 6:
      return False
    return True

emp1 = Employee('Ishu', 'Ramesh', '70000')

import datetime
date = datetime.date(2016,7,11)

print(Employee.is_workday(date))


