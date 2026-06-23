'''
Smallest Multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10
without any remainder.
What is the smallest positive number that is evenly divisible (divisible with no
remainder) by all of the numbers from 1 to 20?
'''
# LCM(1 ~ 20)
# = 2^4 × 3^2 × 5 × 7 × 11 × 13 × 17 × 19
# = 232792560

def is_prime(num):
    """
    判断 num 是否是质数
    """
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def smallest_multiple(n):
    """
    使用质因数最高次幂求 1 ~ n 的最小公倍数
    """
    ans = 1
    for p in range(2, n + 1):
        if is_prime(p):
            power = p
            # 找到不超过 n 的 p 的最高次幂
            while power * p <= n:
                power *= p

            ans *= power
    return ans
ans = smallest_multiple(20)
print(ans)
