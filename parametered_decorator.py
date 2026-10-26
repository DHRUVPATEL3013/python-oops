def logger(role):
  def decorator(func):
    def wrapper(*args,**kwargs):
      print(f"role : {role}")

      result = func(*args,**kwargs)
      return  result
      

    return wrapper
  return decorator

@logger("Admin")
def add(a,b):
  return a+b

result=add(2,5)
print(result)


