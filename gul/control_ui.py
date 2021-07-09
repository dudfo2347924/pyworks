#컨트롤 도구 - 레이블, 버튼, 목록 박스, 입력장치
from  tkinter import *

class App:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        Label(frame, text="제목 ").grid(row=0, column=0)
        Entry(frame, width=20).grid(row=0, column=1)
        Button(frame, text="확인").grid(row=0, column=2)
        # 체크 버튼
        check_var = StringVar()
        check = Checkbutton(frame, text="체크", variable=check_var,
                    onvalue='Y', offvalue='N')

        check.grid(row=1, column=0)

        listbox=Listbox(frame, height = 3, selectmode=SINGLE)
        color=['red', 'green', 'blue', 'yellow']
        for i in color:
            listbox.insert(END, i)
        listbox.grid(row=1, column=1)

        radio_frame = Frame(frame)
        radio_sel = StringVar()
        b1 = Radiobutton(radio_frame, text='왼쪽',
                         variable=radio_sel, value='P')
        b1.pack(side=LEFT)
        b2 = Radiobutton(radio_frame, text='오른쪽',
                         variable=radio_sel, value='L')
        b2.pack(side=LEFT)
        radio_frame.grid(row=1, column=2)

root = Tk()
root.title("컨트롤 도구 UI")
app = App(root)
root.mainloop()