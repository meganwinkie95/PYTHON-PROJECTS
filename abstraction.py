from abc import ABC, abstractmethod
class credit(ABC):
    def creditbill(self, amount):
        print("your credit bill is: ",amount)
#this function is telling us to pass in an argument
    @abstractmethod
    def payment(self, amount):
        pass

class creditcardpayment(credit):
#here we are defining how to implement the payment function
    def payment(self, amount):
        print('Your credit bill of {} has not been paid, and may effect your credit score. '.format(amount))

obj = creditcardpayment()
obj.creditbill("$800")
obj.payment("$800")
