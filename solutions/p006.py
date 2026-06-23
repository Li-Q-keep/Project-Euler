'''
Sum Square Difference
The sum of the squares of the first ten natural numbers is,
1² + 2² + ... +10² = 385.
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... +10)²= 55² =3025.
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385= 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sum_square_difference(n):
    # 利用数学公式计算
    sum_nums = n * (n+1) //2
    sum_square = n * (n+1) * (2*n+1) //6
    return sum_nums **2 - sum_square

print('Ans:', sum_square_difference(100))