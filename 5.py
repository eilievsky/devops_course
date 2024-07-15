
def seven_boom():

    num_lst = list(range(1,101))
    print(num_lst)

    new_lst =  [x for x in num_lst if "7" not in str(x)]
    new_lst =  [x for x in new_lst if (x % 7) != 0]
    print(new_lst)



seven_boom()
