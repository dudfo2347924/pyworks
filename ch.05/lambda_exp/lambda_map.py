li1 = [1,2,3,4,5]

li2 = map(lambda x : x * 3, li1) # map(함수 자료형)
print(list(li2))
print(list(map(lambda x : x * 5, li1)))

li3 = filter(lambda x : x < 4, li1)
print(list(li3))
print(list(filter(lambda x : x < 3, li1)))