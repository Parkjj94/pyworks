# 기본 매개변수 - 매개 변수를 초기화하여 선언
# 함수 호출시에 생략하면 기본값으로 출력

def print_string(text, count=1):
    for i in range(count):
        print(text)


print_string("Hello~")      # count를 생략 호출
print_string("Hello~", 5)