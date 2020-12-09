'''
Author: your name
Date: 2020-11-10 10:43:46
LastEditTime: 2020-12-09 17:39:35
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \YYS-master\gui.py
'''
import tkinter as tk
import time
import yys


def main():
    window = tk.Tk()  # 创建窗口
    window.title("阴阳师助手")  # 窗口标题
    window.geometry('400x400')  # 窗口大小，小写字母x
    window.resizable(0, 0)  # 设置窗口大小不可变

    # 副本模式
    selectModel = tk.StringVar()
    selectModel.set(0)

    logText = tk.Text(window, height=10, width=80, state=tk.DISABLED)

    modelName = ['单人探索', '组队御魂', '业原火', '御灵', '结界突破']
    j = 0
    # 探索单选按钮
    for i in modelName:
        tk.Radiobutton(window, text=i, variable=selectModel,
                       value=j+1).grid(row=int(j/2), column=int(j % 2))
        j = j+1
    if j % 2 != 0:
        j = j + 1

    physicalLimit = tk.StringVar()
    physicalLimit.set(0)
    limitLable = tk.Label(window, text='体力限制：')
    limitText = tk.Entry(window, textvariable=physicalLimit)
    limitLable.grid(row=int(j / 2), column=0)
    limitText.grid(row=int(j / 2), column=1)
    j = j + 2
    costLabel = tk.Label(window, text='体力消耗：')
    costText = tk.Entry(window, textvariable=0, state=tk.DISABLED)
    costLabel.grid(row=int(j / 2), column=0)
    costText.grid(row=int(j / 2), column=1)
    j = j+2
    btn_start = tk.Button(window, text='开始', command=lambda: yys.start(
        logText, costText, btn_start, btn_stop, int(selectModel.get()),  int(physicalLimit.get())))
    btn_start.grid(row=int(j/2), column=0)
    btn_stop = tk.Button(window, text='暂停', command=lambda: yys.stop(
        logText, btn_start, btn_stop))
    btn_stop.grid(row=int(j / 2), column=1)

    j = j+2
    logText.grid(row=int(j/2), column=0, columnspan=4)
    # 以上是窗口的主体
    window.mainloop()  # 结束（不停循环刷新）


if __name__ == '__main__':
    main()
