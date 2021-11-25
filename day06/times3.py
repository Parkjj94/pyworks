# 1~100까지의 수 중에서 배수  출력

def times(x):
    #3의 배수
    global count
    for n in range(1, 101):
        if n % x == 0:
            count += 1
            print(n, end=' ')
            #print(count)

count = 0
(times(3))
print("\n3의 배수의 개수 : " +  str(count) + "개")