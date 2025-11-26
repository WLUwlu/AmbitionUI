#coding=utf-8
from tkinter import *
from tkinter import messagebox


root=Tk()

root.title("我的第一个gui")

btn01=Button(root)
root.geometry("500x300+100+200")

btn01["text"]="点我就送花"

btn01.pack()      #窗口压缩

def songhua(e):   #e就是事件对象
    messagebox.showinfo("Message","送你一朵花,亲亲我吧")
    print("送你99朵玫瑰花")
btn01.bind("<Button-1>",songhua)

root.mainloop()  #调用组件的mainloop()方法,进入事件循环
