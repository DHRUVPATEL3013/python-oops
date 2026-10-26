class A:
  def hello(self):
    print("A")

class B:
  def hello(self):
    print("B")

class C(A,B):
  pass



c=C()
c.hello()
print(C.mro())
 