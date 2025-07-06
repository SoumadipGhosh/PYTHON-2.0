# def add(a,b): # paramertres..
#     x=a+b
#     return x

# c=add(10,20) # arguments..
# print(c)

# defaullt arguments..

# def add(a,b,plus=0): # now plus is not zero it is 3..
#     x=a+b+plus
#     return x

# c=add(10,20,3)
# print(c)

# keyword arguments..

def add(a,b,plus=0): # now plus is not zero it is 3..
    x=a+b+plus
    return x
c=add(a=10,b=20,plus=3) # here we are using keyword argument..
print(c)