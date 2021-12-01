# Dog 클래스 만들기
class Dog:
    # tricks = []     # 클래스 리스트 합쳐서 출력하려면 이 곳에 선언

    def __init__(self, name):
        self.name = name
        self.tricks = []        # 인스턴스 멤버 리스트

    def add_tricks(self, trick):
        self.tricks.append(trick)

dog1 = Dog("Elsa")
dog2 = Dog("buddy")

dog1.add_tricks("play dead")
dog2.add_tricks("roll over")

print(dog1.tricks)
print(dog2.tricks)