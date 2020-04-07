# Implementing fizz buzz
# Replaces numbers divisible by 3 with fizz
# Replaces numbers divisible by 5 with buzz
# Replaces numbers divisible by 3 and 5 as fizzbuzz

# New function to do fizzbuzz
def our_fizz_buzz(my_range) :
    """Takes a range of number and prints the numbers replaced by fizz if the number is divisible by 3
    and buzz if divisible by 5. Or fizzbuzz if divisible by both 3 and 5."""

    for fb in my_range :
        if fb % 3 == 0 and fb % 5 == 0 :
            print("fizzbuzz")
        elif fb % 3 == 0 :
            print("fizz")
        elif fb % 5 == 0 :
            print("buzz")
        else:
            print(fb)

# Try the function
our_fizz_buzz(range(1,20))


# Here if we wanted to do it printing the number and the fizz or buzz label
# New function to do fizzbuzz
def number_fizz_buzz(my_range) :
    """Takes a range of number and prints the numbers followed by fizz if the number is divisible by 3
    and buzz if divisible by 5. Or fizzbuzz if divisible by both 3 and 5."""

    for fb in my_range :
        if fb % 3 == 0 and fb % 5 == 0:
            print(str(fb) + " fizzbuzz")
        elif fb % 3 == 0:
            print(str(fb) + " fizz")
        elif fb % 5 == 0:
            print(str(fb) + " buzz")
        else:
            print(fb)

# Try the function
number_fizz_buzz(range(1,20))


# From class, to do it by actually returning something
def fizzbuzz():
    for fizzbuzz in range(1,20):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            fizzbuzz = "fizzbuzz"
        elif fizzbuzz % 3 ==0:
            fizzbuzz = "fizz"
        elif fizzbuzz % 5 == 0:
            fizzbuzz = "buzz"
        yield fizzbuzz

# Will create a list generator
fizzbuzz()
list(fizzbuzz())
set(fizzbuzz())

# Another example from class

def fizzbuzz(x):
    """Takes a number
    Returns a number or fizz if divisible by 3, buzz if divisible by 5,
    fizzbuzz if divisible by both """
    return (
        "Fizzbuzz" if x % 3 == 0 and x % 5 == 0
        else "Fizz" if x % 3 == 0
        else "Buzz" if x % 5 == 0
        else x
    )

fizzbuzz(16)

# List comprehension
[fizzbuzz(x) for x in range(1,19)]

# Could do it the old fashion way by initializing a list
def fizzbuzz_list(x):
    """A simple implementation of fizzbuzz"""
    my_list = []
    for i in x:
        if i % 3 == 0 and i % 5  == 0:
            my_list.append("fizzbuzz")
        elif i % 3 == 0:
            my_list.append("fizz")
        elif i % 5 == 0:
            my_list.append("buzz")
        else:
            my_list.append(i)
    return my_list

fizzbuzz_list(range(1,20))



# Functions from gitter
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fizzbuzz(iterable):
    return (
        "fizz" * (i % 3 == 0)
        + "buzz" * (i % 5 == 0)
        or str(i)
        for i in iterable
        if i
    )


def pipeline(data, funcs):
    for f in funcs:
        data = f(data)
    return data


list(pipeline(9, [fib, fizzbuzz]))
# ['1', '1', '2', 'fizz', 'buzz', '8', '13', 'fizz']