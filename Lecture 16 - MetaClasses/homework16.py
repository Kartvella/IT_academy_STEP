#Exercise N1
def check_positive(func):
    def wrapper(num):
        if num < 0:
            raise ValueError('number must be positive')
        result = func(num)
        print(f"result: {result}")
        return result
    return wrapper

@check_positive
def return_num(num):
    return num

try:
    return_num(3) 
    return_num(-3)  
except ValueError as e:
    print(e)


#Exercise N2

class PositiveCheck:
    def __call__(self, func):
        def wrapper(num):
            if num < 0:
                raise ValueError("the number must be positive.")
            result = func(num)
            print(f"result: {result}")
        return wrapper

positive_check= PositiveCheck()

@positive_check
def return_number(num):
    return num

try:
    return_number(3) 
    return_number(-3)  
except ValueError as e:
    print(e)



#Exercise N3

import time

def timer(func):
    def wrapper(x): 
        start_time = time.time()
        func(x)
        total_time = time.time() - start_time
        print(f"time that '{func.__name__}' function took was {total_time:.3} seconds") 
    return wrapper

@timer
def calculate(x):
    count = 0
    for i in range(x):
        count +=i
    return count

calculate(100_000_000)

#Exercise N4

class LoggingMeta(type):
    def __new__(cls, name, bases, class_dict):
        methods = [key for key, value in class_dict.items() if callable(value)]
        
        print(f"created class - '{name}'")
        print(f"methods: {methods}")
        
        return super().__new__(cls, name, bases, class_dict)

class ExampleClass(metaclass=LoggingMeta):
    def method_one(self):
        pass

    def method_two(self):
        pass

class TestClass(metaclass=LoggingMeta):
    def method1(self):
        pass

    def method2(self):
        pass