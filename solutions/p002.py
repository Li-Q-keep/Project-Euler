# P2
'''
考虑该斐波那契数列中不超过四百万的项，求其中为偶数的项之和。
'''
def sol1(max_num):
    # 穷举
    i,j =1,1
    sum_num =0
    while j<=max_num:
        if j%2==0:
            sum_num +=j
        tmp =i
        i =j
        j =tmp +j
    return sum_num

def sol2(max_num):
    # Fibonacci sequence每隔两个奇数出现一个偶数
    # 已知连续的两个偶Fibonacci数 x,y，则下一个数为x+4y
    # 迭代更快
    x,y =0,2
    sum_num =0
    while y<=max_num:
        sum_num +=y
        tmp =x
        x =y
        y =tmp + 4*y
    return sum_num

if __name__=="__main__":
    max_num =10**6 *4
    print('Sol1: ',sol1(max_num)) # 4613732
    print('Sol2: ',sol2(max_num)) # 4613732