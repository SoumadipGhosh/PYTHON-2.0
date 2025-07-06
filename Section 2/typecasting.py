a=34
b="34" 
d=233 # d is an integer
num_str="12"
# a is an integer and b is a string



print(a)
print(type(a))

print(b)
print(type(b))

# convert b to an integer

c=int(b)  # Typecasting: converting string to integer
print(c)
print(type(c))

e=str(d) # Typecasting: converting integer to string
print(e)
print(type(e))

num_int=int(num_str) # Typecasting: converting string to integer
print(num_int)
print(type(num_int))

pi=3.14
pi_int=int(pi)
print(pi_int) # 3..14 is converted to 3
print(type(pi_int))