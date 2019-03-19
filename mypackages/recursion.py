def sum_array(array):

    list =0
    for i in array:
        total= total + i
        '''Return sum of all items in array'''
        return list

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
    '''Return nth term in fibonacci sequence'''
    return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        '''Return n!'''
        return n * factorial(n - 1)

def reverse(word):
    rev = word[::-1]
    '''Return word in reverse'''
    return rev
