# 빵 - 55개, 우유 = 38개, 사람 12명



bread = 55
milk = 38
person = 12

#1인당 할당되는 빵과 우유의 개수
print("빵의 개수 : ", int(bread / person))
print("우유의 개수 : ", int(milk / person))

#남는 빵과 우유의 개수
print("남는 빵의 개수 : ", int(bread % person))
print("남는 우유의 개수 : ", int(milk % person))
