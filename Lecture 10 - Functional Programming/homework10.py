#Exercise N1
def zipped(lst1, lst2):
    if len(lst1) == len(lst2):
        return zip(lst1, lst2)
    else:
        return "list's must have same lenght"
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
zipp = zipped(lst1, lst2)
if type(zipp) == zip:
    print(list(zipp))
else:
    print(zipp)

#Exercise N2
even = lambda lst: [x for x in lst if x % 2 == 0]
nums = [i for i in range(1, 21)]
print(even(nums))


#Exercise N3


positive = lambda lst: list(filter(lambda x: x > 0, lst))

nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
print(positive(nums))

#Exercise N4

palindrome = lambda string: bool(filter(lambda string: string == string[::-1], string))

string = 'racecar'
print(palindrome(string))


#Exercise N5
from functools import reduce

# Exercise N5
num_lst = [1, 2, 3, 4]

try:
    num_func = lambda a, b: a * b
    if not all(isinstance(num, (int, float)) for num in num_lst):
        raise TypeError("elements must be int or float")
    
    result = reduce(num_func, num_lst)
    print(result)

except TypeError as e:
    print(e)

# Exercise N6
ending = lambda str_list, string: list(filter(lambda char: string in char, str_list))
lst = ['hello', 'world', 'coding', 'nod']
try:
    if not isinstance(string, str):
        raise TypeError("The second argument must be a string.")
    if not all(isinstance(item, str) for item in lst):
        raise TypeError("elements in list must be string type")
    
    result = ending(lst, 'ing')
    print(result)

except TypeError as e:
    print(e)
