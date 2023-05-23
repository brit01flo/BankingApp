import random

class Register:

    def __init__(self, name, surname, email, password):
        self.account = Register.generateAccountNo()
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.balance = 0


    def __str__(self) -> str:
        return f"{self.account}, {self.name}, {self.surname}, {self.email}, {self.password}, {self.balance}"


    def generateAccountNo():
        accountNo = '89'
        for i in range(10):
            accountNo += str(random.randrange(0, 9, 1))
        return accountNo