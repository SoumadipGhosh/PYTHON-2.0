a=int(input("enter no 1 : "))
b=int(input("enter no 2 : "))
    

try:
    c=a/b
    print(c)

except Exception as e:
    print(c)
    
finally: # this is always executed ..whenever a error come or not .. 
    print("This is always executed ..")            