from tkinter import  *

def click():
    print("hello~ python")

root = Tk()
root.title("hello")#루트

frame= Frame(root)
frame.pack()

Button(frame, text="확인", command = click).grid(row=0,column=0)

root.mainloop()