# [P9] Special Pythagorean Triplet

A Pythagorean triplet is a set of three natural numbers, $a <b < c$, for which,

$$
a^2+b^2=c^2
$$

For example, $3^2+4^2=9+16= 25=5^2$.
There exists exactly one Pythagorean triplet for which a +b+ c = 1000.
Find the product $abc$.

---

## 暴力解法

```python
# solutions/p009.py
def find_Pythagorean_Triplet(target):
    '''
    暴力求解
    Input: sum of the Pythagorean triplet
    Output: the Pythagorean triplet a,b,c
    '''
    # a < b < c, so a < target/3, b < (target-a)/2
    for a in range(1, target // 3):
        for b in range(a + 1, (target - a) // 2 + 1):
            c = target - a - b
            if a * a + b * b == c * c:
                return a, b, c
    return None
```

## 代数化简，一层循环

设 $a+b+c=x$，则有

$$
\begin{aligned}
a^2+b^2 &=(x-(a+b))^2\\
&=x^2+a^2+b^2+2ab-2x(a+b)\\
\therefore\quad 2(x-a)b+ &2ax-x^2=0,\quad b =\frac{x^2-2ax}{2(x-a)}
\end{aligned}
$$

```python
# solutions/p009_1.py
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
```

## 勾股数生成公式

$$
\begin{aligned}
a &= k(m^2 - n^2)\\
b &= k(2mn)\\
c &= k(m^2 + n^2)\\
\end{aligned}
$$

因此，$a+b+c=2km(m+n)$。仅需枚举$m,n$检验是否$2m(m+n)$可整除即可

```python
# solutions/p009_2.py
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
```