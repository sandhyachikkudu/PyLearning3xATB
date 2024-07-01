class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__private_var=100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, balane):
        self.balance += balane

    def __withdraw(self, balance):
        self.balance -= balance

    def __show_balance(self):
        print("your balance",self.balance)

    def if_you_are_auth(self,flag):
        if flag:
            print("you are authorised")
            self.__show_balance()
        else:
            print("you are not authorised")


    def if_you_are_auth_user(self,auth,balance):

        if auth:
            self.__withdraw(balance=balance)
        else:
            print("you are not authorised")



jp= BankAccount()
jp.deposit(100)
secrete_pass = input("Enter your secret password to see the balance: ")
if secrete_pass == "123":
    jp.if_you_are_auth(True)
else:
    jp.if_you_are_auth(False)
secrete_pass = input("Enter your secret password to withdraw: ")
your_amount = int(input("Enter your amount to withdraw: "))
if secrete_pass == "123":
    jp.if_you_are_auth_user(True,balance=your_amount)
    jp.if_you_are_auth(True)

else:
    jp.if_you_are_auth_user(False)


# jp.if_you_are_auth(True)
# jp.if_you_are_auth_user(True,10)
# jp.if_you_are_auth(True)




# a1=BankAccount()
# print(a1.balance)
# a1.deposit(100)
# a1.show_balance()
# a1.withdraw(10)
# a1.show_balance()