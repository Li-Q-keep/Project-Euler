'''
Special Pythagorean Triplet
A Pythagorean triplet is a set of three natural numbers, a <b < c, for which,
a²+b²=c²
For example,3²+4²=9+16= 25=5².
There exists exactly one Pythagorean triplet for which a +b+ c = 1000.
Find the product abc.
'''

def find_Pythagorean_Triplet(target):
    '''
    勾股数生成式
    a = k(m^2 - n^2)
    b = k(2mn)
    c = k(m^2 + n^2)<target, so m<sqrt(target/2)
    '''

    m =2
    while 2 * m * m < target:
        for n in range(1, m):
            denominator = 2 * m * (m + n)
            if target % denominator == 0:
                k = target // denominator
                a = k * (m * m - n * n)
                b = k * (2 * m * n)
                c = k * (m * m + n * n)

                # 公式生成出来的 a, b 不一定满足 a < b，所以排序
                a, b, c = sorted([a, b, c])
                return a, b, c
        m += 1
    return None

if __name__ == "__main__":
    triplet = find_Pythagorean_Triplet(1000)
    if triplet:
        a, b, c = triplet
        product = a * b * c
        print(f"The Pythagorean triplet is: a={a}, b={b}, c={c}")
        print(f"The product abc is: {product}")
    else:
        print("No Pythagorean triplet found for the given sum.")