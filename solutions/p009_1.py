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
    代数化简，一层循环
    '''
    for a in range(1, target // 3):
        b = (target * (target - 2 * a)) // (2 * (target - a))
        c = target - a - b
        if a * a + b * b == c * c:
            return a, b, c
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