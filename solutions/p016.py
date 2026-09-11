"""
Project Euler Problem 16: Power Digit Sum (幂的数字和)
=======================================================
问题描述：
    2^15 = 32768，各位数字之和为 3+2+7+6+8 = 26。
    求 2^1000 的各位数字之和。

关键观察：
    2^1000 约 302 位十进制数。Python int 支持任意精度。
"""


# ========================================
# 思路：
#   Python 的 int 无位数限制，直接计算 2**1000。
#   转为字符串后遍历每个字符，转回 int 求和。
#
# 时间复杂度：O(d)，d 为位数（约 302=1000lg2）
# 空间复杂度：O(d)
# =====================================================================

def solve_direct(exponent=1000):
    """直接计算 2^exponent 的各位数字之和"""
    power = 2 ** exponent
    return sum(int(digit) for digit in str(power))


# ==================== 大基数表示法（模拟大数库原理）====================
# 思路：
#   真实大数库（GMP、Java BigInteger）通常以 2^32 或 10^9 为基数存储。
#   这里以 10^9 为基数（每"位"存 9 个十进制数字），大幅减少数组长度。
#   2^1000 约 302 位，用 10^9 基数只需约 34 个"大位"。
#
# 时间复杂度：O(d' × exponent)，d' 为大位数量
# 优点：更接近真实大数库实现。
# =====================================================================

BASE = 10 ** 9
def solve_large_base(exponent=1000, base=2):
    """使用大基数（10^9）模拟大数乘法"""
    digits = [1]  # 每个元素代表 BASE^i 位上的值
    
    for _ in range(exponent):
        carry = 0
        for i in range(len(digits)):
            product = digits[i] * base + carry
            digits[i] = product % BASE
            carry = product // BASE  # 进位，由于base=2，carry最多为1
        if carry > 0:
            digits.append(carry)
    
    # 求各位数字之和：每个大位内部还有 9 个十进制数字
    total = 0
    for i, num in enumerate(digits):
        if i == len(digits) - 1:  # 最高位可能不足 9 位
            while num > 0:
                total += num % 10
                num //= 10
        else:  # 中间位固定 9 位
            for _ in range(9):
                total += num % 10
                num //= 10
    return total


if __name__ == "__main__":
    exponent = 1000
    print("直接计算法：2^{} 的各位数字之和 = {}".format(exponent, solve_direct(exponent))) #1366
    print("大基数模拟法：2^{} 的各位数字之和 = {}".format(exponent, solve_large_base(exponent)))