numbers=[1,2,34,55,21]

def square(x):
    return x*x

# new=map(square,numbers) # give a map type ..
new=list(map(square,numbers))
print(new)