# 예외 처리(Exception 클래스)

try:
    x = int(input("숫자를 입력하세요 : "))
    print(x)
except ValueError:
#except ValueError as e: 생략 가능 except만 써도 됨.
    print("유효한 숫자가 아닙니다. 숫자를 입력하세요")