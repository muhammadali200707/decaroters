def say_hello(text):
    return text.upper()


"""print(say_hello('hello'))"""

obj1 = say_hello

""" print(obj1('hello'))"""


def upper(info: str) -> str:
    return info.upper()


def lower(info: str) -> str:
    return info.lower()


def greet(function):
    greeting = function("""Hi,\n I am created by a function passed as an argument.""")
    print(greeting)


"""greet(upper)
greet(lower)"""


def create_adder(first_number: int):
    def adder(second_number: int) -> int:
        return first_number + second_number

    return adder


find_100 = create_adder(90)
"""print(f"This is the answer ->  {find_100(10)}")"""


def hello_decorator(func):
    def inner1():
        print("Hello, this is before function execution")

        func()

        print("This is after function execution")

    return inner1


def function_to_be_used():
    print("This is inside the function !!")


function_to_be_used = hello_decorator(function_to_be_used)

"""function_to_be_used()"""


def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")

        returned_value = func(*args, **kwargs)
        print("after Execution")

        return returned_value

    return inner1


@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


a, b = 4, 6


# print("Sum of the numbers =", sum_two_numbers(a, b))


def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner


def decor(func):
    def inner():
        x = func()
        return 2 * x

    return inner


@decor1
@decor
def num():
    return 10


@decor
@decor1
def num2():
    return 10


print(num())
print(num2())
