# from dataclasses import dataclass

# @dataclass
# class User:
#   name:str
#   age:int
#   email:str


# user1=User(name="Dhruv",age="hello",email="d@gmail.com")
# user2=User(name="Dhruv",age=23,email="d@gmail.com")

# print(user1 == user2)
# print(user1 is user2)

# print(user1)

class User:
  def __init__(self,name,age,email):
    self.name=name
    self.age=age
    self.email=email

  def __repr__(self):
    return f"User(name='{self.name}',age={self.age},email='{self.email}')"


user1=User(name="Dhruv",age=23,email="d@gmail.com")
user2=User(name="Dhruv",age=23,email="d@gmail.com")

print(user1 == user2)
print(user1 is user2)


print(user1.__dict__)


