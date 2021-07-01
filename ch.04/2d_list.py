d1 = [1, 2, 3]

print(d1[0])
d1.append(10)
print(d1)

d2 = [[4], [5], [6]]
print(d2[0][0])
d2.append([40])
print(d2)

d2.append([d2[0][0] + d2[1][0] + d2[2][0] + d2[3][0]])


for i in d2:
    print([i][0])

avg = (d2[0][0] + d2[1][0] + d2[2][0] + d2[3][0])/4
d2.append([avg])
print(d2)