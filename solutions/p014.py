"""
Project Euler Problem 14: Longest Collatz Sequence

The following iterative sequence is defined for the set of positive integers:
n -> n/2 (n is even)
n ->3n+1(n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 -> 40-> 20 ->10->5 ->16->8 -> 4 -> 2 ->1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it
has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NoTE: Once the chain starts the terms are allowed to go above one million.
"""


# ==================== 暴力法 ====================
# 思路：对每个起始数字，完整模拟 Collatz 过程直到变为 1，统计步数。
# 缺点：大量重复计算。例如 13 和 26 的序列后半段完全相同，但会分别计算。
# 时间复杂度：O(N * L)，L 为平均序列长度
# =======================================================

def collatz_length_naive(n):
    """计算从 n 开始的 Collatz 序列长度（包含 n 和 1）"""
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length


def solve_naive(limit=1_000_000):
    """暴力求解：遍历每个数字，计算序列长度"""
    max_length = 0
    best_start = 1
    for start in range(1, limit):
        length = collatz_length_naive(start)
        if length > max_length:
            max_length = length
            best_start = start
    return best_start, max_length

# ==================== 迭代缓存（自底向上）====================
# 思路：用迭代代替递归实现记忆化。
# 在前进过程中记录路径，遇到已缓存数字后倒推填充路径上所有数字的缓存。
# 优点：避免递归开销和深度限制。
# ===================================================================

def solve_iterative(limit=1_000_000):
    """迭代缓存法求解"""
    cache = {1: 1}
    max_length = 0
    best_start = 1

    for start in range(1, limit):
        n = start
        path = []  # 记录当前路径上未缓存的数字

        # 沿着 Collatz 序列前进，直到遇到已缓存的数字
        while n not in cache:
            path.append(n)
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1

        # 从已知长度处倒推，填充路径上所有数字的缓存
        length = cache[n]
        for num in reversed(path):
            length += 1
            cache[num] = length

        if cache[start] > max_length:
            max_length = cache[start]
            best_start = start

    return best_start, max_length

# ==================== 位运算 + 列表缓存====================
# 思路：
# 1. 用位运算 n & 1 判断奇偶，比 n % 2 更快
# 2. 用 n >> 1 代替 n // 2，位运算更高效
# 3. 用列表缓存小于 limit 的所有数字，O(1) 索引访问
# 4. 迭代过程中记录完整路径，倒推填充缓存，最大化缓存命中率
# 时间复杂度：接近 O(N)，空间复杂度：O(N)
# 这是综合性能最优的版本。
# =======================================================================

def solve_ultimate(limit=1_000_000):
    """位运算优化的迭代缓存法（推荐）"""
    cache = [0] * limit
    cache[1] = 1

    max_len = 0
    best = 1

    for i in range(1, limit):
        n = i
        seq = []  # 记录路径上的数字

        # 沿序列前进，直到遇到已缓存的数字
        # 注意：n 可能暂时大于 limit，但最终会落回 < limit 的已缓存区域
        while n >= limit or cache[n] == 0:
            seq.append(n)
            if n & 1:      # 奇数：位运算判断
                n = 3 * n + 1
            else:          # 偶数
                n >>= 1    # 位运算除以 2

        # 倒推填充缓存
        length = cache[n]
        for num in reversed(seq):
            length += 1
            if num < limit:
                cache[num] = length

        if cache[i] > max_len:
            max_len = cache[i]
            best = i

    return best, max_len


if __name__ == "__main__":
    print("Project Euler Problem 14: Longest Collatz Sequence")
    ans_naive = solve_naive()
    print(f"暴力法结果: 起始数字 {ans_naive[0]}, 序列长度 {ans_naive[1]}")
    ans_iterative = solve_iterative()
    print(f"迭代缓存法结果: 起始数字 {ans_iterative[0]}, 序列长度 {ans_iterative[1]}")
    ans_ultimate = solve_ultimate()
    print(f"位运算优化法结果: 起始数字 {ans_ultimate[0]}, 序列长度 {ans_ultimate[1]}")