def get_my_number(number):
    a = number ** 2
    b =  number ** 0.5
    c =  number % 2 ==0
    return a,b,c

a,*b = get_my_number(41)
print(a)
print("test of changes")
print(b)
