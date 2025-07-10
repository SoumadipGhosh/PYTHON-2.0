# def very_slow_func():
#     print("something ...")
#     print("something ...")
#     print("something ...")
#     print("something ...")
#     print("something ...")
#     return 80

# a=very_slow_func()
# use of walrus operator ..
# if(a:=very_slow_func()>10):
#     print(a)
    
# else:
#     print("it is not greater than 10..")    

while(data:=input("Enter the val : ")): # use of walrus operator ..
    print(data)
    if data=="q":
        break
    