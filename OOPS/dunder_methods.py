class User:
  def __init__(self):
    self.name="Dhruv"
    self.age=23

  def __str__(self):
    return f"User(name : {self.name},age : {self.age})"

  def __repr__(self):
      return f"User({self.name},{self.age})"



user=User()

ls=[
   user,user
]

print(ls.__str__())

print(repr(ls))