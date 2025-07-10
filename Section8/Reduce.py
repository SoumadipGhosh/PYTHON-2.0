from functools import reduce

no=[1,23,4,5,6]

def sum(a,b):
    return a+b

c=reduce(sum,no)
print (c)