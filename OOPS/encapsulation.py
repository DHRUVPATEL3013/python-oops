class Account:
  def __init__(self,balance):
    self.balance=balance




  def deposit(self,balance):
    self.balance += balance

  def withdraw(self,balance):
      if balance <=0:
         raise ValueError("balance can not be less than 0")

      if balance >self.balance:
               raise ValueError("insufficient amount")
      
      self.balance += balance




account=Account(5000)


# account.balance=9000
# print(account.balance)




class User():
    company="Promettuer"
    @staticmethod
    def valid_email(email):
        return "@" in email

    @classmethod
    def company_logo(cls):

        print(cls.company)


user=User()
User.company_logo()






