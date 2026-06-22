def is_even(num):
    """ this function returm whether the number is odd or even """

    if num % 2 == 0:
        return 'even'

    else:
        return 'odd'

#calling function
for i in range(1,11):
    x = is_even(i)
    print(i , x)
