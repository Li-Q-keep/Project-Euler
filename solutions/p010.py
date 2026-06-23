'''
Summation of Primes
The sum of the primes below 10 is 2+3+5+7=17.
Find the sum of all the primes below two million.
'''

from utils.prime import sieve_of_eratosthenes

def sum_of_primes_below(limit):
    '''
    Use Sieve of Eratosthenes to find all primes below limit, then sum them up.
    '''
    primes = sieve_of_eratosthenes(limit)  # Get all primes below limit
    return sum(primes)

print('Ans:', sum_of_primes_below(2000000))  # 142913828922