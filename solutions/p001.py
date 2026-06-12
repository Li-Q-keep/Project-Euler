# P1
'''
Find the sum of all the multiples of 3 or 5 below 1000.
'''
import math
# sol1与sol2函数均可解
def sol1(max_num,min_num=0):
    # <max_num的所有3或5倍数之和
    sum_num =0
    for i in range(min_num,max_num):
        if i%3==0 or i%5==0:
            sum_num +=i
    return sum_num

def sol2(max_num,min_num=0):
    # <max_num的所有3或5倍数之和
    # 3的倍数之和
    max_num =max_num-1 # 不包括max_num
    max3 =max_num//3
    min3 =math.ceil(min_num//3)
    sum3 =3* (max3+min3)*(max3-min3+1)/2
    # 5的倍数之和
    max5 =max_num//5
    min5 =math.ceil(min_num//5)
    sum5 =5* (max5+min5)*(max5-min5+1)/2
    # 15的倍数之和
    max15 =max_num //15
    min15 =math.ceil(min_num//15)
    sum15 =15* (max15+min15) *(max15-min15+1) /2
    sum_num =sum3+sum5-sum15
    return sum_num

if __name__=="__main__":
    max_num =1000
    print('Sol1:',sol1(max_num))
    print('Sol2:',sol2(max_num))