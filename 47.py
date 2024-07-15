try:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    result =  number1/number2
    print("result is " + result)
except TypeError as e:
    print("could not cast")
except BaseException as e:
    print(f"something else {e.args}")

