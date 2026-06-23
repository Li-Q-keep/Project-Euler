'''
10001st Prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
'''

def find_nth_prime(n):
    '''
    思路：只用已经找到的素数试除
    '''
    prime_ls =[2]
    candidate = 3 # 从3开始检查
    while len(prime_ls) < n:
        is_prime = True
        for p in prime_ls:
            if p*p >candidate:
                break
            if candidate %p ==0:
                is_prime =False
                break
        if is_prime:
            # 列表中的质数均非其因子
            prime_ls.append(candidate)
        candidate += 2 # 所有偶数都不是质数
    return prime_ls[-1]

print('Ans:',find_nth_prime(10001)) # 104743
        