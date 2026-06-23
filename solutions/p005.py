'''
Smallest Multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10
without any remainder.
What is the smallest positive number that is evenly divisible (divisible with no
remainder) by all of the numbers from 1 to 20?
'''

def gcd(a, b):
    """计算两个数的最大公约数(辗转相除法/欧几里得算法)"""
    while b:
        a, b = b, a % b # 两个整数的最大公约数等于其中较小的数和两数的相除余数的最大公约数。
    return a

def lcm(a, b):
    """计算两个数的最小公倍数"""
    return a * b // gcd(a, b)

def smallest_multiple(n):
    """计算1到n的最小公倍数"""
    multiple = 1
    for i in range(2, n + 1):
        multiple = lcm(multiple, i)
    return multiple

print(f"1到20的最小公倍数是: {smallest_multiple(20)}")