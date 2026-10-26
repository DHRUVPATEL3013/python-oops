def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1 - before")
        
        result = func(*args, **kwargs)
        
        print("Decorator 1 - after")
        
        return result
    
    return wrapper


def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2 - before")
        
        result = func(*args, **kwargs)
        
        print("Decorator 2 - after")
        
        return result
    
    return wrapper


@decorator1
@decorator2
def hello():
    print("hello")

hello()