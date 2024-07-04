class myCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

balane =100
withdraw = int(input("Enter amount to withdraw: "))
if withdraw > balane:
    raise Exception("Withdrawal exceeded and balance is low")
else:
    print("Withdrawal is good")
    print("remail balnce",(balane-withdraw))