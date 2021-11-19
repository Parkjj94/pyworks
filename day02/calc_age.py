#나이 계산 프로그램

current_year = 2021
birth_year = int(input("태어난 년도를 입력하세요 : "))
#print(birth_year)

#나이 계산
# 콤마 대신 +를 쓰는경우 숫자를 문자형으로 바꿔줘야함
age = current_year - birth_year + 1
print("당신의 나이는 " + str(age) + "세 입니다.")
