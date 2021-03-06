# 절대값 함수 구현하기
import math

#절대값 알고리즘1
def my_abs(x):
    if x < 0:
        return -x
    else:
        return x

#절대값 알고리즘2
def my_abs2(x):
    y = x * x
    return int(math.sqrt(y))

print(my_abs(-3))  #3
print(my_abs2(-3))  #3
print(abs(-3))