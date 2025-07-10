def sum(*args):
    # return(args)
    # args doesnt care about how many argument you pass..
    total=0
    for item in args:
        total+=item # add all items ..
    return total    
    

print(sum(2,3,4,23)) # give me error beacuse sum function have only 2 arguments ..