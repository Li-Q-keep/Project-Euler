'''
Maximum Path Sum I

Triangle data (15 rows):

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

def sol_max_path_sum_reverse(triangle: list) -> int:
    '''
    Find the maximum total from top to bottom of the triangle.
    '''
    # 从倒数第二行开始，逐行向上更新每个元素的最大路径和
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])
    return triangle[0][0]

def sol_max_path_sum(triangle: list) -> int:
    '''
    Find the maximum total from top to bottom of the triangle.
    '''
    # 从上到下更新每个元素的最大路径和
    for row in range(1, len(triangle)):
        for col in range(len(triangle[row])):
            if col == 0:
                triangle[row][col] += triangle[row - 1][col]
            elif col == len(triangle[row]) - 1:
                triangle[row][col] += triangle[row - 1][col - 1]
            else:
                triangle[row][col] += max(triangle[row - 1][col - 1], triangle[row - 1][col])
    return max(triangle[-1])

if __name__ == "__main__":
    triangle = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
    ]
    triangle_copy = [row[:] for row in triangle]  # Create a copy of the triangle for the second method
    print('Ans:', sol_max_path_sum_reverse(triangle))
    print('Ans:', sol_max_path_sum(triangle_copy))