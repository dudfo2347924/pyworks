from tkinter import  *

def click():
    en_text = entry.get()
    text.delete(0.0, END)
    text.insert(END, en_text + "님 환영합니다.")


root = Tk()
root.title("hello")#루트
root.geometry("200x150+200+200")

frame= Frame(root)
frame.pack()

Label(frame,text = '이름 : ').grid(row=0,column=0)
entry = Entry(frame, width=10)
entry.grid(row=0,column=1)
Button(frame, text="확인", command = click).grid(row=1,columnspan=2)

text = Text(frame, width=20, height = 5)
text.grid(row=2, columnspan=2)

root.mainloop()