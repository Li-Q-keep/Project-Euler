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
    # 直接计算
    sum_nums =0
    sum_square =0
    for i in range(1,n+1):
        sum_nums +=i
        sum_square += i*i
    return sum_nums **2 - sum_square

print('Ans:', sum_square_difference(100))