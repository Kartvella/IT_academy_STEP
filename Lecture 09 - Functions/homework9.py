#Exercise N1

int_list = [10,20,30,40]
def add(num):
    int_list.append(num)
    return int_list
numm = add(50)
print(numm)


#Exercise N2

def func(number: int) -> int:
    if number == 1:
        return 1
    return number + func(number - 1)
funcc = func(5)
print(funcc)


#Exercise N3

def reverse(string):
    if len(string) == 0:
        return string
    return string[-1] + reverse(string[:-1])
    
esrever = reverse('gnirts')
print(esrever)


#Exercise N4

def fib_list(n):
    lst = []
    def fib(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    for i in range(n):
        lst.append(fib(i))
    return lst
fibb = fib_list(10)
print(fibb)