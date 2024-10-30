class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"name: {self.name}, deposit: {self.deposit}, loan: {self.loan}"

class House:
    def __init__(self, ID, price, owner):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = "for sale"

    def sell_apartment(self, buyer, loan_amount=0):
        if buyer.deposit >= self.price:
            self.owner.deposit += self.price 
            buyer.deposit -= self.price
            self.owner = buyer 
            self.status = "sold"
            print(f"Apartment {self.ID} sold to {buyer.name} for ${self.price}.")
        elif loan_amount > 0 and buyer.deposit + loan_amount >= self.price:
            self.owner.deposit += self.price 
            buyer.deposit -= self.price 
            buyer.loan += loan_amount
            self.owner = buyer
            self.status = "sold with a loan"
            print(f"apartment {self.ID} sold to {buyer.name} for ${self.price} with a loan of ${loan_amount}.")
        else:
            print(f"{buyer.name} cannot afford the apartment {self.ID}, insufficient funds.")

owner = Person(name="Alice", deposit=1000)
buyer = Person(name="Bob", deposit=0)

house = House(ID="A101", price=2000, owner=owner)

print(owner) 
print(buyer) 

print(f'current owner - {house.owner.name}')

buyer.deposit += 3000
print(f'buyer balance after deposit - ${buyer.deposit}')  # 3000

house.sell_apartment(buyer)
print(f'current owner - {house.owner.name}')


print(owner) 
print(buyer) 
