"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primesHelper(number):
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


def primes(number_of_primes):
    list = []
    tester = 2
    while len(list) != number_of_primes:
        if (primesHelper(tester)):
            list.append(tester)
            tester += 1
        else:
            tester += 1
    return list
