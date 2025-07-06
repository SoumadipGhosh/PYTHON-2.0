class Employee: # class ..
    company ="HP"
    
    def get_salary(self): # function ..
        return 34000      # self : basically e and e2..refers the object of the class ..
    
e1=Employee() # object ..
print(e1.get_salary())    

e2=Employee() # make onother object ..
print(e2.get_salary())

print(e2.company)