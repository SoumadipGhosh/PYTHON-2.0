class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    @property # property decorater..
    def first_name(self):
        l = self.name.split(" ")  # split the name into 2 parts ..
        return l[0] # print 1st part ..
    
    @first_name.setter
    def first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}" 
        self.name = new_name

e = Employee("Jack Doe", 34555)
# print(e.first_name())
# e.set_first_name("John")
# print(e.name)

print(e.first_name)
e.first_name = "John" # john change to jack ..
print(e.name)