#Exercise N1

def is_anagram(string: str, string2: str) -> bool:
    return ''.join(sorted(string.lower())) == ''.join(sorted(string2.lower()))
string = input('enter a word: ')
string2 = input('enter a word: ')
print('they are anagram: ', is_anagram(string, string2))


#Exercise N2

def counted(string: str, symbol: str) -> tuple:
    counter = 0
    for char in string.lower():
        if char == symbol:
            counter +=1
    return string, symbol, counter
a, b, c = counted(string='Every evening, we see the serene sea reflecting the endless sky', symbol='e')
print(f'"{b}" in "{a}" was found {c} times')


#Exercise N3

def fibonacci(x:int) -> list:
    if x < 0:
        print('number must be positive')
    lst = []
    a, b = 0, 1
    
    while a <= x:
        lst.append(a)
        a, b = b, a + b 
    return lst

x = int(input('enter a number: '))
print(f'fibonacci numbers up to {x}: ',fibonacci(x))