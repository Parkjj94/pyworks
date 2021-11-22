#3의 배수 구하기(1~20) 합계와 평균

count = 0
sum = 0
for i in range(1, 21):
    if i % 3 == 0:
        count += 1
        sum += i
        print("3의 배수 =", i)
# i = 3, count = 0 + 1
# i = 6, count = 1 + 1
avg = sum / count
print()
print("3의 배수의 개수 :", count)
print()
print("3의 배수의 합계 :", sum)
print()
print("3의 배수의 평균 :", avg)