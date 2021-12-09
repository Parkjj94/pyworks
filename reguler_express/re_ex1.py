import re

# compile() - > byte 코드로 바꿈, 함수의 매개 변수로 정규식 사용
p = re.compile("[a-z]+")        # [a-z]+ 범위 안에 반복되는 영어소문자
m = p.match("afternoon")        # match() 첫 문자가 일치하면 결과를 반환, 일치하지 않으면 None을 반환
print(m)

m2 = p.match("2021 python")
print(m2)

s = p.search("2021 python") # 전체를 검색해서 일치하면 결과를 반환
print(s)