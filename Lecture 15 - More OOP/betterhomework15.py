class BankAccount:
    def __init__(self):
        self.balance = 1000 
        self.loan = 0

    def __str__(self):
        return f'balance: ${self.balance}, loan: ${self.loan}'

    def deposit_money(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'deposited: ${amount} to , new balance: ${self.balance}')
        else:
            print("amount must be a positive number")

    def take_loan(self, house, loan_amount):
        if house.price <= self.balance:
            return "u have enough balance and don't need a loan"
        elif loan_amount + self.balance < house.price:
            return "loan amount is insufficient to purchase the house"
        else:
            self.loan += loan_amount
            self.balance += loan_amount
            print(f"loan taken: ${loan_amount}. New balance: ${self.balance}")


class Person:
    def __init__(self, name, bank_acc):
        self.name = name
        self.bank_acc = bank_acc

    def __str__(self):
        return f"name: {self.name}, {self.bank_acc}"


class House:
    def __init__(self, id, price, owner: Person):
        self.id = id
        self.price = price
        self.owner = owner
        self.status = 'for sale'

    def __str__(self):
        return f"house price: ${self.price}, status: {self.status}, owner: {self.owner.name}"

    def sell(self, customer: Person, loan_amount=0):
        if customer.bank_acc.balance >= self.price:
            self.owner.bank_acc.balance += self.price
            customer.bank_acc.balance -= self.price
            print(f'previous owner - {self.owner.name}, new owner - {customer.name}')
            self.owner = customer
            self.status = 'sold'
            print("house was sold without loan")
        elif loan_amount > 0 and customer.bank_acc.balance + loan_amount >= self.price:
            customer.bank_acc.take_loan(self, loan_amount)
            self.owner.bank_acc.balance += self.price
            customer.bank_acc.balance -= self.price
            self.owner = customer
            self.status = 'sold with loan'
            print("house sold with loan")
        else:
            print("insufficient funds or loan amount")
bank_acc_owner = BankAccount()
bank_acc_customer = BankAccount()

owner = Person('John', bank_acc=bank_acc_owner)
customer = Person('Jannet', bank_acc=bank_acc_customer)

house = House('Aa12', 2000, owner)

print(f'current owner - {house.owner.name}')

customer.bank_acc.deposit_money(3000)

print(f'customer balance - ${customer.bank_acc.balance}')

house.sell(customer=customer)

print(f'current owner - {house.owner.name}')
print(f'owner balance - ${owner.bank_acc.balance}')
print(f'customer balance - ${customer.bank_acc.balance}')
print(f'customer loan - ${customer.bank_acc.loan}')