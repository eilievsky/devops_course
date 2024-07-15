def fin(n):
    a,b = 0,1
    while b<n:
        print(b)
        a,b = b,a+b

def fib2(n):
    result = []
    a,b = 0,1
    while b<n:
        result.append(n)
        a,b = b,a+b
    return result

def get_numeric(number):
    numbers = ["zero","one","two","three","four"]
    if number < len(numbers):
        return numbers(number)
    else:
        return "not supported"

a=6
def my_function(x):
    print(x*a)
def my_function(x,a):
    print(x*a)

def my_function2(x,a):
    print(x*a)

