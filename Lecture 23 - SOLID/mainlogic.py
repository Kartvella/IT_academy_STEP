class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })

    def total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.items)

    def remove_item(self, name):
        self.items = [item for item in self.items if item['name'] != name]

    def is_empty(self):
        return len(self.items) == 0