#영어 타자 게임
import random
import time

word = ['sky', 'earth', 'moon', 'flower', 'tree', 'strawberry', 'grape', 'garlic', 'onion', 'potato']

# w = random.choice(word)

n = 1 # 문제 번호
f = 0 # 오답 횟수
input("[타자게임] 준비되면 엔터! ")
start = time.time()
while n < 11:
        print('-문제', n)
        question = random.choice(word)  #문제 단어 출제
        print(question)
        answer = input()        #답을 입력
        # 통과 아니면 오타 코드 작성
        if answer == question:
            print("통과입니다!")
            n += 1
        else:
            print("오타! 다시 도전!")
            f += 1

end = time.time()
print("오답 횟수 : ", f, "회")
print("게임 소요 시간 : %.2f초" % (end-start))
