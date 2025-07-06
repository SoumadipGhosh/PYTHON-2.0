def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a) # say_hello come here ..
        return wrapper
    return decorator        

@repeat(7)
def say_hello(a):
    print(f"hello {a}")
    
say_hello("harry")