# Converter 클래스 정의
# 온도 변환기 : 화씨온도(F) = 섭씨온도(C) x 1.8 + 32
from day09.class_lib.scaleconverter import ScaleConverter

class Converter(ScaleConverter):        # 스케일컨버터 상속받음
    def __init__(self, units_from, units_to, factor, offset):
        super().__init__(units_from, units_to, factor)  # 'C', 'F', 1.8
        self.offset = offset    # 32

    def convert(self, value):       # 부모 레서드 재정의(overriding)
        return self.factor * value + self.offset        #(단위값 x 수) + 단위2 값

conv = Converter('C', 'F', 1.8, 32)
print("Converting 21C")
#print(str(conv.convert(21)) + conv.units_to)
print("%.2fF" % conv.convert(21))