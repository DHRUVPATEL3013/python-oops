class PaymentService():
  def pay(self):
    print("payment is paid by payment service")


class Order():
  def __init__(self,name):
    self.orders=[]
    self.name=name
    self.payment=PaymentService()

  def place_order(self):
    self.payment.pay()
    print("order placed")

  def __eq__(self, other):
    return self.name == other.name

  def __len__(self):
    return len(self.orders)


  def __str__(self):
    return f"Name is {self.name}"

  def __repr__(self):
        return f"Name is {self.name}"

    

    



order1=Order("Dhruv")
order2=Order("Dhruv")

# print(order1 == order2 )
# print(order1.__len__())

print(order1)
print(order1.__repr__())



