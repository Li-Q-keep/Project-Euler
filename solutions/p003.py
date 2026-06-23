'''
Largest Prime Factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
'''

def largest_prime_factor(num):
    '''
    + 一个合数n必然有一个质因数不超过√n
    + 从最小的质数2开始试除，如果能整除就不断除尽
    + 最后剩下的如果大于1，那就是最大的质因数
    '''
    i = 2
    while i*i <= num:
        if num % i == 0:
            num //= i
        else:
            i += 1 if i == 2 else 2
    return num

if __name__ == "__main__":
    num = 600851475143
    print("Largest prime factor:", largest_prime_factor(num)) # 6857