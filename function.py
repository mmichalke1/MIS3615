def print_lyrics():
    print('hey jude')
    print('take a sad song and make it better')

# print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print('na-na-na-na\n'*10)
    print_lyrics()

# repeat_lyrics()

def print_twice(whatever):
    print(whatever)
    print(whatever)

whatever = 'matt'
# print_twice(whatever)

name = 'matty'

# print_twice(name)

def give_a_break():
    s = 'break'
    return s

# print(give_a_break())
#
# print_twice(give_a_break())

b = give_a_break()
# print(b[0])

def calc(a, b):
    s = a + b
    return  s
calc(1,2)
# print(calc(1,2))

import random
def my_abs(n):
    if n >0:
        return n
    else:
        return -n

# num = (input("select number"))
# print(my_abs(int(num)))

def quadratic(a,b,c):
    import math
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        x_1 = (-b + math.sqrt(discriminant))/(2*a)
        x_2 = (-b - math.sqrt(discriminant))/(2*a)
        return  x_1, x_2
    else:
        return None, None


# input_a = float(input('Number A: '))
# input_b = float(input('Number B: '))
# input_c = float(input('Number C: '))
#
# sol_1, sol_2 = quadratic(input_a, input_b, input_c)
# if sol_1:
#     print('results are: {} and {}' .format(sol_1, sol_2))
# else:
#     print('no real number solutions')

# path_1 = 10
# path_2 = 5
#
# if path_1<path_2:
#     take(path_1)
# else:
#     take(path_2)

def fib(n):
    if n == 2 or n == 1:
        return 1
    else:
        # print('in calc', n)
        return fib(n-2) + fib(n-1)

print(fib(int(input("Fib number: "))))

def F(n):
    import math
    return ((1+math.sqrt(5))**n-(1-math.sqrt(5))**n)/(2**n*math.sqrt(5))

print(F(int(input('fib number: '))))
