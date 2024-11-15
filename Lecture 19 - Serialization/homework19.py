#Exercise N1

import json
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"name: {self.name}, price: {self.price}, quantity: {self.quantity}"

def custom_serializer(product):
    if isinstance(product, Product):
        return {
            "name": product.name,
            "price": product.price,
            "quantity": product.quantity
        }
    raise TypeError("object of type Product is not JSON serializable")

def custom_deserializer(json_obj):
    return Product(json_obj['name'], json_obj['price'], json_obj['quantity'])

product_list = [
    Product("laptop", 1500, 5),
    Product("mouse", 20, 50),
    Product("keyboard", 30, 30)
]

json_data = json.dumps(product_list, default=custom_serializer, indent=4)
with open('Lecture 19 - serialization/products.json', 'w') as file:
    file.write(json_data)

print("serialized JSON Data:")
print(json_data)

with open('Lecture 19 - serialization/products.json', 'r') as file:
    loaded_products = json.load(file, object_hook=custom_deserializer)

print("\ndeserialized Product Objects:")
for product in loaded_products:
    print(product)


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
