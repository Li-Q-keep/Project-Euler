'''
Largest Prime Factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
'''
import numpy as np
def sieve_of_eratosthenes(limit):
    """
    埃拉托斯特尼筛法：生成所有小于等于limit的质数
    思路：从小到大标记合数，剩下的就是质数
    """
    is_prime = np.ones(limit + 1, dtype=bool)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            # i是质数，标记所有i的倍数
            # j = 
            # 小于i*i的倍数已经被更小的质数标记过了，所以从i*i开始
            # for j in range(i * i, limit + 1, i):
            is_prime[(i*i):(limit+1):i] = False
    
    # 收集所有质数
    primes = [i for i in range(2, limit + 1) if is_prime[i]]
    return primes


def largest_prime_factor(n, primes=None):
    """
    筛法优化：预生成质数列表，然后用质数试除
    
    参数:
        n: 要分解的数
        primes: 预生成的质数列表，如果为None则动态生成
    """
    if primes is None:
        # 动态生成到sqrt(n)的质数
        primes = sieve_of_eratosthenes(int(n**0.5) + 1)
    
    max_prime = -1
    
    # 用预生成的质数试除
    for p in primes:
        if p * p > n:
            break
        while n % p == 0:
            max_prime = p
            n //= p
    
    # 如果n>1，说明n是大于sqrt(原n)的质数
    if n > 1:
        max_prime = n
    
    return max_prime

# 预生成质数列表（可复用）
primes = sieve_of_eratosthenes(int(600851475143**0.5) + 1)
print(f"预生成质数数量: {len(primes)} (到 {primes[-1]})")
print(f"600851475143 的最大质因数: {largest_prime_factor(600851475143, primes)}")
