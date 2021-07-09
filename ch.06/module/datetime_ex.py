import datetime

now = datetime.datetime.now()
#print(now)

print("{}년".format(now.year))
print("{}월".format(now.month))
print("{}일".format(now.day))
print("{}시".format(now.hour))
print("{}분".format(now.minute))
print("{}초".format(now.second))


print(now.strftime("%Y년 %M월 %d일 %h시 %m분 %s초")format())