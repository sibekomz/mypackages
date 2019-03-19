def sum_array(array):
    '''Return sum of all items in array'''
    list =0
    for i in array:
        total= total + i
        return list

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

        for n in fibonacci(n):
            print (str(n))

    '''Return nth term in fibonacci sequence'''

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1

    else:
        return n * factorial(n - 1)

    '''Return n!'''

def reverse(word):

    '''Return word in reverse'''
    rev = word.split()
    rev = rev[-1::-1]
    result = " ".join(rev)
    return result
