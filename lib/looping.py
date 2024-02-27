#!/usr/bin/env python3

def happy_new_year():
    n = 10
    while n >= 1:
        n -= 1
        print(n + 1)
    print("Happy New Year!")

def square_integers(int_list):
    int_list = [n * n for n in int_list]
    return int_list
def fizzbuzz():
    n = 1
    while n <= 100:
        if (n % 3 == 0) and (n % 5 == 0):
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)
        n += 1
