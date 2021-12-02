# 입력 받아 파일 쓰기

with open('input.txt', 'a') as f:       # a 추가 모드
    text = input("저장할 내용을 입력해주세요 : ")
    f.write(text)
    f.write('\n')