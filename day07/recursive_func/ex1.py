# 재귀함수 - 자기가 자신을 호출하는 함수
def sos(n):
    for i in range(n):
        print("Help me!!")


def sos2(n):
    if n < 1:
        return ""  # 0 일때는 안 찍음
    else:
        print("Help me!!")
        return sos2(n-1)


#sos(5)
sos2(5)  #Help me
#sos2(4) #Help me
#sos2(3) #Help me
#sos2(2) #Help me
#sos2(1) #Help me
#sos2(0) #공백을 출력
