# 가변 매개변수 예제

def merge_text(*text):
    sum_s = ""          # 숫자는 초기화할때 0을 두지만, 문자 초기화시 공백문자로 놔둔다
    for s in text:
        sum_s += s
    return sum_s


str1 = merge_text("봄", "여름")
str2 = merge_text("봄", "여름", "가을", "겨울")

print(str1)
print(str2)