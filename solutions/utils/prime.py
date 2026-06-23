'''
关于质数的工具函数
'''

import numpy as np

# @ p003_1.py
def sieve_of_eratosthenes(limit):
    """
    埃拉托斯特尼筛法：生成所有小于limit的质数
    思路：从小到大标记合数，剩下的就是质数，只筛奇数
    """
    is_prime = np.ones(limit//2, dtype=bool)
    is_prime[0] = False # 对应数字1
    
    for p in range(3, int(limit**0.5) + 1, 2): # p=3对应坐标1
        i = p//2 # 当前坐标
        if is_prime[i]:
            start = (p * p) // 2 # 从p*p开始标记，小于p*p的已被之前的质数标记过了
            is_prime[start::p] = False # 标记所有p的倍数（p^2+2k*p)为合数
    
    # 收集所有奇数质数
    primes = [2*i+1 for i in range(len(is_prime)) if is_prime[i]]
    return [2] + primes

if __name__ == "__main__":
    limit = 100
    primes = sieve_of_eratosthenes(limit)
    print(f"Primes below {limit}: {primes}")