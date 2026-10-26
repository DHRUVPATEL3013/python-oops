# def logger(func):
#   def wrapper(*args,**kwargs):
#     print("function is starting")
#     func(*args,*kwargs)
#     print("function is finished")
#   return wrapper

# @logger
# def greeting(name):
#   print(f"hello {name}")

# greeting("Dhruv")



# def logger(func):
#   def wrapper(*args,**kwargs):
#     print("function is starting")
#     a=func(*args,**kwargs)
#     print(a)
#     print("function is finished")
#     return a

#   return wrapper

# @logger
# def add(a,b):
#   return a+b


# a=add(1,7)



def logger(func):
  def wrapper(*args,**kwargs):
    print("function is started")
    print(f"Arguments : {args}")
    print(f"key value Arguments : {kwargs}")

    re=func(*args,**kwargs)
    print(re)
    print("function is finished")
    return re
    
  return wrapper

@logger
def add(a,b):
  return a+b

result=add(3,6)
print(f"final result : {result}")

