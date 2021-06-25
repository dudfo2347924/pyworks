#threading 모듈

import threading

def function_a():
    print("5초간격으로 반복 실행")
    timer = threading.Timer(5,function_a)
    timer.start()

function_a()