from converter import ScaleConverter
#단위 변환 클래스 확장
#온도변환 : 화씨온도(F) = 섭씨온도(C)*1.8 + 32

class Converters(ScaleConverter):
    def __init__(self,units_from,units_to,factor,offset):
        super().__init__(units_from,units_to,factor)
        self.offset = offset

    def convert(self,val):
        return self.factor * val + self.offset

con = Converters('C','F',1.8,32)
print("Converting 40")
print(str(con.convert(40)) + con.units_from)