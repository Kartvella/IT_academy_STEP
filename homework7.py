#Exercise N1

squared_numbers = set()
for i in range(1, 11):
    squared_numbers.add(i**2)
print(squared_numbers)


#Exercise N2

user_input = input("enter some text: ")
sett = set()
for char in user_input:
    sett.add(char)
print(sett)


#Exercise N3

tuple1 = (1,2,3,4,5,6)
tuple2 = (4,5,5,6,6,7)

combined_tuple = tuple(set(tuple1 + tuple1))
duplicated_values = list()
for i in tuple1:
    if i in tuple2:
        duplicated_values.append(i)

print('combined_tuple: ', combined_tuple)
print('duplicated_values: ', duplicated_values)


#Exercise N4

tuple3 = (1, 2, 3, 4, 5, 6, 7, 8, 9)

my_list = list(tuple3)

my_list[0], my_list[-1] = my_list[-1], my_list[0]

modified_tuple = tuple(my_list)

print(modified_tuple)


#Exercise N5
tuple4 = (1, (2, 3), (4, (5, 6)))

list4 = list(tuple4)
empty_list = []

while list4:
    item = list4.pop(0)
    if isinstance(item, tuple):
        list4 += list(item) 
    else:
        empty_list.append(item)

tupled4 = tuple(sorted(empty_list))

print(tupled4)

#Exercise N6

set1 = {1, 2}
set2 = {'a', 'b'}

for i in set1:
    for char in set2:
        tuple5 = (i, char)
        print(tuple5)