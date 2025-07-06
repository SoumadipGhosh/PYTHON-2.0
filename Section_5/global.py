def sum(a,b):
    print("hey i am summing ")
    c=a+b
    # dont use exessive use of global variabe ..
    global z # pls update global z ..when we need to change the global variable ..
    z=2 # now it is refer to the global z ..not local variable ..
    return c

z=3 # global var..
print(sum(3,4))
print(z) # 3