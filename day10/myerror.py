# 예외 만들기
# Exception 클래스를 상속받아야함

class MyError(Exception):
    #pass
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보' or nick == '칠푼이' or nick == '멍청이':
        raise MyError()     # 에러 발생
    print(nick)

try:
    say_nick('영웅')
    say_nick('바보')
except MyError as e:    # e는 MyError의 별칭 객체
    print(e)