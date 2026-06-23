'''
10001st Prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
'''

from utils.prime import sieve_of_eratosthenes

def find_nth_prime(n):
    '''
    Use Sieve of Eratosthenes, Find a appropriate limit(20000)
    '''
    limit = 200000
    primes = sieve_of_eratosthenes(limit)
    return primes[n - 1]

print('Ans:',find_nth_prime(10001)) # 104743