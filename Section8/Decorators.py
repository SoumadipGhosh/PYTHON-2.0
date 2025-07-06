# decorator is a function and it contains also function known as wrapper ..
def decorator(func):
    def wrapper():
        print("I am about to execute a function")
        func()
        print("I am execute this function")
    return wrapper    

@decorator
def say_hello():
    print("hello")

say_hello()   