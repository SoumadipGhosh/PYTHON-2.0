def sum(a,b):
    c=a+b
    z=1 # create a local variable ,after the function is return ..
    # local variable in function and acess only inside the  function ..
    return c

def greet():
    z=32 # local variable ..
    print("Hello")

z=8 # z is a global variable .. it declared outside the function ..so acess from anywhere..
print(sum(2,3)) 
print(z) # print8 beacuse 1 is destroy ..
