'''
Largest Palindrome Product
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009=91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(n):
    """判断一个数是否是回文数"""
    s = str(n)
    return s == s[::-1]

def largest_palindrome_product(n_digits):
    max_range = 10 ** n_digits -1
    min_range = 10 ** (n_digits - 1)
    max_palindrome = 0
    for i in range(max_range, min_range, -1):
        for j in range(i, min_range, -1):  # 从i开始避免重复计算
            product = i * j
            if product <= max_palindrome:
                break  # 如果乘积已经小于当前最大回文数，后续也不会更大了
            if is_palindrome(product):
                max_palindrome = product
    return max_palindrome

print(f"最大的回文数是: {largest_palindrome_product(3)}")