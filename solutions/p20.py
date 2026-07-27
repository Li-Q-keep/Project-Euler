'''
Factorial Digit Sum
n! means n x(n- 1) x... x 3 x 2 x 1.
For example,10! = 10x 9 × ... × 3 x 2 x1= 3628800,
and the sum of the digits in the number 10! is 3+6+2+8+8+0+0=27.
Find the sum of the digits in the number 100!.
'''

def factorial_digit_sum(n: int) -> int:
    '''
    列表法模拟大数计算
    '''
    # 初始化一个列表来存储大数的每一位数字
    digits = [1]  # 初始值为1，即0!和1!的结果
    for i in range(2, n + 1):
        carry = 0
        for j in range(len(digits)):
            product = digits[j] * i + carry
            digits[j] = product % 10  # 更新当前位的数字
            carry = product // 10  # 计算进位
        while carry > 0:
            digits.append(carry % 10)  # 将进位的每一位添加到列表中
            carry //= 10
    return sum(digits)

import math
def factorial_digit_sum_math(n: int) -> int:
    """
    计算 n! 的各位数字之和
    :param n: 非负整数
    :return: 各位数字之和
    """
    # 计算 n 的阶乘（Python 自动处理大整数）
    factorial_result = math.factorial(n)
    # 将阶乘结果转换为字符串，遍历每个字符并求和
    digit_sum = sum(int(digit) for digit in str(factorial_result))
    return digit_sum

if __name__ == "__main__":
    n = 100
    result = factorial_digit_sum(n)
    result_math = factorial_digit_sum_math(n)
    print(f"The sum of the digits in the number {n}! is: {result}") # Ans: 648
    print(f"The sum of the digits in the number {n}! is: {result_math}") # Ans: 648