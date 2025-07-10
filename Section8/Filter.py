def is_greater_than_9(x):
    if x>9:
        return True
    else:
        return False

a=[12,2,3,45,7,8,11,43]

new=list(filter(is_greater_than_9 , a)) # it is basically filter the a ..
print(new)