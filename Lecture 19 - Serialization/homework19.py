import json

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }

    @classmethod
    def from_dict(cls, data):
        return cls(name=data['name'], price=data['price'], quantity=data['quantity'])

def serialize_products(products, filename='products.json'):
    try:
        with open(filename, 'w') as json_file:
            json.dump([product.to_dict() for product in products], json_file, indent=4)
    except Exception as e:
        print(f'error occurred during serialization: {e}')

def deserialize_products(filename='products.json'):
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
            return [Product.from_dict(item) for item in data]
    except Exception as e:
        print(f"error occurred during deserialization: {e}")
        return []

products = [
    Product(name="Wireless Bluetooth Headphones", price=59.99, quantity=120),
    Product(name="Stainless Steel Water Bottle", price=19.99, quantity=350),
    Product(name="Organic Cotton T-Shirt", price=25.00, quantity=200),
    Product(name="Portable Power Bank 10000mAh", price=29.99, quantity=150),
    Product(name="Adjustable Ergonomic Office Chair", price=249.99, quantity=50),
    Product(name="LED Desk Lamp with USB Charging Port", price=39.99, quantity=85),
    Product(name="Smart Home Wi-Fi Plug", price=14.99, quantity=400)
]

serialize_products(products)

loaded_products = deserialize_products()

for product in loaded_products:
    print(product.__dict__)

#Exercise N2

with open('Lecture 19 - serialization/movies.json', 'r') as file:
    data = json.load(file)

movies_over_2000_new_crime = []
movies_before_2000_old_drama = []
movies_in_2000_new_century = []

for page in data:
    for movie in page['results']:
        release_year = int(movie['release_date'].split('-')[0])

        if release_year > 2000 and 'Crime' in movie['genres']:
            movie['genres'] = ['New_Crime' if genre == 'Crime' else genre for genre in movie['genres']]
            movies_over_2000_new_crime.append(movie)

        elif release_year < 2000 and 'Drama' in movie['genres']:
            movie['genres'] = ['Old_Drama' if genre == 'Drama' else genre for genre in movie['genres']]
            movies_before_2000_old_drama.append(movie)

        elif release_year == 2000:
            movie['genres'].append('New_Century')
            movies_in_2000_new_century.append(movie)

modified_movies = {
    'movies_over_2000_new_crime': movies_over_2000_new_crime,
    'movies_before_2000_old_drama': movies_before_2000_old_drama,
    'movies_in_2000_new_century': movies_in_2000_new_century
}

with open('Lecture 19 - serialization/movies.json', 'w') as file:
    json.dump(modified_movies, file, indent=4)
