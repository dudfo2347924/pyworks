# 조건 : 현금,카드가 있으면 택시를 타고, 아니면 걸어간다.

money = int(input("현금이 얼마나 있습니까?"))
card = True

if money>4000 or card :
    print("택시를 탄다.")
else :
    print("걸어간다.")

