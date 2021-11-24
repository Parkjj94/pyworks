#체질량 지수 bmi 계산하기 (bmi = 몸무게 / 키 x 키) (내가 한 것 - 문제점:소수점)

name = input("이름을 입력하세요 : ")
cm = int(input("키를 입력하세요 : "))
kg = int(input("몸무게를 입력하세요 : "))
bmi = kg / ((cm * cm) / 10000)

if bmi < 20:
    print(name, "님의 bmi는 ", bmi, "입니다.")
    print("저체중입니다.")
elif bmi >= 20 and bmi <= 24:
    print(name, "님의 bmi는 ", bmi, "입니다.")
    print("정상입니다.")
elif bmi >= 25 and bmi <= 29:
    print(name, "님의 bmi는 ", bmi, "입니다.")
    print("과체중입니다.")
else:
    print(name, "님의 bmi는 ", bmi, "입니다.")
    print("비만입니다.")

# bmi 지수 계산 (강사님이 하신 것)
name = input("이름을 입력하세요 : ")
height = float(input("키(cm)를 입력하세요 : "))
height = height / 100
weight = float(input("몸무게(kg)를 입력하세요 : "))

bmi = weight / (height * height)

print("{}님의 bmi는 {}입니다.".format(name, bmi))
print("{}님의 bmi는 {:.2f}입니다.".format(name, bmi))
print("%s님의 bmi는 %.2f입니다" % (name, bmi))
if bmi < 20:
    print("저체중입니다.")
elif bmi < 25:
    print("정상입니다.")
elif bmi < 30:
    print("과체중입니다.")
else:
    print("비만입니다.")

# %d(정수), %f(실수), %s(문자열)
# "문자열 포맷" % 변수(상수) 변수가 두개면 괄호해주고 콤마