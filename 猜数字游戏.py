# -*- coding: utf-8 -*-
# 程序说明:
# 创建时间: 2022/1/9 15:

from tkinter import *
from random import randint


class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.pack()
        self.master = master
        self.creater()
        self.difficult = "1"

    def creater(self):
        self.text1 = Text(self, width=40, height=12)
        self.text1.grid(row=0, rowspan=4, column=0, columnspan=4, pady=4)
        self.text1.insert(1.0, ">>>Hello\n")
        self.text1.insert(2.0, ">>>点击下面的按钮")
        self.entry2 = Entry(self, width=30, state="disabled")
        self.entry2.grid(row=4, column=0, columnspan=3, pady=20)
        Button(self, text="提交答案", command=self.commit, state="disabled").grid(row=4, column=3, padx=10)
        Button(self, text="开始游戏", command=self.main).grid(row=5, column=0, padx=2, sticky=EW)
        Button(self, text="结束游戏", command=self.end).grid(row=5, column=1, padx=2, sticky=EW)
        Button(self, text="难度提升", command=self.difficulter).grid(row=5, column=2, padx=2, sticky=EW)
        Button(self, text="游戏玩法", command=self.gameplay).grid(row=5, column=3, padx=2, sticky=EW)

    def main(self):
        self.text1.delete(1.0, END)
        self.text1.insert(1.0, ">>>已重置游戏\n")
        Button(self, text="提交答案", command=self.commit).grid(row=4, column=3, padx=10)
        self.entry2 = Entry(self, width=30)
        self.entry2.grid(row=4, column=0, columnspan=3, pady=20)
        self.i = 1
        self.text1.insert(2.0, ">>>开始游戏\n")
        if self.difficult == "1":
            self.x = randint(0, 10)
            self.text1.insert(3.0, ">>>请猜0-10之间的数，你有5次机会\n")
            print(self.x)
        elif self.difficult == "2":
            self.x = randint(0, 20)
            self.text1.insert(3.0, ">>>请猜0-20之间的数，你有5次机会\n")
            print(self.x)
        elif self.difficult == "3":
            self.x = randint(0, 30)
            self.text1.insert(3.0, ">>>请猜0-30之间的数，你有5次机会\n")
            print(self.x)
        elif self.difficult == "4":
            self.x = randint(0, 40)
            self.text1.insert(3.0, ">>>请猜0-40之间的数，你有5次机会\n")
            print(self.x)
        elif self.difficult == "5":
            self.x = randint(0, 50)
            self.text1.insert(3.0, ">>>请猜0-50之间的数，你有5次机会\n")
            print(self.x)
        elif self.difficult == "6":
            self.x = randint(0, 60)
            self.text1.insert(3.0, ">>>请猜0-60之间的数，你有5次机会\n")
            print(self.x)
        elif self.difficult == "7":
            self.x = randint(0, 70)
            self.text1.insert(3.0, ">>>请猜0-70之间的数，你有5次机会\n")
            print(self.x)
        elif self.difficult == "8":
            self.x = randint(0, 80)
            self.text1.insert(3.0, ">>>请猜0-80之间的数，你有5次机会\n")
            print(self.x)
        elif self.difficult == "9":
            self.x = randint(0, 90)
            self.text1.insert(3.0, ">>>请猜0-90之间的数，你有5次机会\n")
            print(self.x)
        elif self.difficult == "10":
            self.x = randint(0, 100)
            self.text1.insert(3.0, ">>>请猜0-100之间的数，你有5次机会\n")
            print(self.x)

    def commit(self):
        y = self.entry2.get()
        if y == str(self.x):
            self.text1.insert(END, ">>>恭喜你猜对了\n")
            self.text1.insert(END, ">>>点击开始游戏即可重新开始\n")
            Button(self, text="提交答案", command=self.commit, state="disabled").grid(row=4, column=3, padx=10)
        elif y != str(self.x):
            if int(y) > self.x:
                self.text1.insert(END, ">>>你猜大了(还有{}次机会)\n".format(5-self.i))
                self.i += 1
            else:
                self.text1.insert(END, ">>>你猜小了(还有{}次机会)\n".format(5 - self.i))
                self.i += 1
            if self.i == 6:
                self.text1.insert(END, ">>>游戏结束")
                self.entry2.delete(0, END)
                self.entry2.insert(END, "点击重新开始游戏")
                Button(self, text="提交答案", command=self.commit, state="disabled").grid(row=4, column=3, padx=10)

        else:
            self.text1.insert(4.0, ">>>无效数字")

    def end(self):
        sys.exit()

    def difficulter(self):
        Scale(self, from_=1, to=10, length=500, tickinterval=5, orient=HORIZONTAL, command=self.text2).grid(row=6, column=0, columnspan=4)

    def text2(self, value):
        self.difficult = value

    def gameplay(self):
        self.text1.delete(1.0, END)
        self.text1.insert(1.0, "游戏名:猜数字\n当前版本:v1.0.2\n玩法:点击开始游戏即可开始，选择难度完后点击开始难度即可。\n更新日志:\n")
        with open("./error/changelog.txt") as f:
            for i in f.readlines():
                self.text1.insert(END, i)


root = Tk()
root.geometry("500x300")
root.title("猜数字 v1.0.2")
app = App(master=root)
root.mainloop()

