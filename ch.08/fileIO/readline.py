
with open("2021kbo.txt", "w") as f:
    team = ['삼성', 'LG', '기아', '롯데']
'''
   for i in team:
       f.write(i + '\n')

with open("2021kbo.txt","r") as f:
   # data = f.readlines()
   # print(data)
    #이차원 리스트 만들기
    for i in range(4):
        data = f.readline().split()
        print(data)
    d2 = []
    for i in range(4):
        d2.append(f.readline().split())

'''