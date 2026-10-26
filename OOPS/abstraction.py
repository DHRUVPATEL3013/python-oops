from abc import ABC,abstractmethod


class PaymentService(ABC):

  @abstractmethod
  def pay(self):
    pass

class UPI(PaymentService):

  def pay(self):
    print("payment by UPI")



class CreditCard(PaymentService):

  def pay(self):
    print("payment by CreditCard")


upi=UPI()
creditCard=CreditCard()

def make_payment(payment_type):
  payment_type.pay()


make_payment(upi)

