while True:
    try:
       a=int(input("enter no 1 : "))
       b=int(input("enter no 2 : "))
    #    print(f"The sum is {a+b}")
       print(f"The division is{a / b}")
       
    except ValueError:
       print("pls dont do this man..") 
       
    except ZeroDivisionError:
       print("hey dont devide by 0")
              
    except Exception as e: 
       print("Error come " , e) # e just print the what the exception is coming ..
       
# using try and except the code will never be crashed .. they show erroe ..    