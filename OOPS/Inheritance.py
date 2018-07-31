class Employee:
  raise_amt = 2
  
  def __init__(self,name,last,pay):
    self.name = name
    self.last = last
    self.pay = pay
    
  def fullname(self):
    return '{}{}'.format(self.name,self.last)
    
  def apply_sal(self):
    self.pay = int(self.pay * self.raise_amt)
    
class Developer(Employee):
    def __init__(self,name,last,pay,prog_lang):
        super(Developer,self).__init__(name,last,pay)
        self.prog_lang = prog_lang

dev_1 = Developer('Ishu', 'Ramesh' , '70000', 'Python')
dev_2 = Developer('Kiran' ,'Parhad', '70000','Java')

print(dev_1.name)
print(dev_2.prog_lang)


