class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def email(self):
        return f'{self.fname}.{self.lname}@gmail.com'

    @property
    def fullname(self):
        return f'{self.fname} {self.lname}'

    @fullname.setter
    def fullname(self, name):
        fname, lname = name.split(' ')
        self.fname = fname
        self.lname = lname

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.fname = None
        self.lname = None


emp = Employee('Adam', 'Smith')
#setter property
emp.fullname = "Hankar Mustapha"

print(emp.fname)
print(emp.lname)
print(emp.fullname)
print(emp.email)
#name deleter property
del emp.fullname
print(emp.fullname)
