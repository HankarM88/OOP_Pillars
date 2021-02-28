class Person:
    who='Ali'
    # init method or constructor
    def __init__(self, name,age,adress):
        self.name = name
        self.age=age
        self.adress=adress
    # Sample Method
    def say_hello(self):
        print('Hello World, my name is', self.name)
    def whomai(self):
        return f'My name is{self.name}',end='\n',
        'my age is{self.age}',end='\n','I live in {self.adress}'

p = Person('Korrit',43,'Agadir')
#acess a class attribute
print(p.who) # or Person.who
#acess an instance attribute
print(p.name)
#acess  instance methods
p.say_hello()
p.whomai()
