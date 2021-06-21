
#자리 배치도 프로그램

customer_num = int(input("입장객의 수 입력 : "))
col_num = int(input("좌석 열의 수 입력 : "))


if customer_num % col_num == 0:
    row_num = int(customer_num / col_num)
elif customer_num % col_num != 0:
    row_num = int(customer_num / col_num + 1)
    
'''print("%d개의 줄이 필요합니다." % row_num)'''

print('자리배치도')

for i in range(0, row_num):
    for j in range(1,col_num+1):
        seats = i*col_num+j
        if seats > customer_num:
            break;
        print(seats, end = ' ')
        
    print()
