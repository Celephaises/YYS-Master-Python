"""
Author: your name
Date: 2020-11-10 10:43:46
LastEditTime: 2020-12-10 14:35:08
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \YYS-master\gui.py
"""
import tkinter as tk

import yys


def main():
    window = tk.Tk()  # 创建窗口
    window.title("阴阳师助手")  # 窗口标题
    window.geometry('400x300')  # 窗口大小，小写字母x
    window.resizable(0, 0)  # 设置窗口大小不可变
    # 副本模式
    selectModel = tk.StringVar()
    selectModel.set(0)

    logText = tk.Text(window, height=10, width=80, state=tk.DISABLED)

    modelName = ['单人探索', '组队御魂', '业原火', '御灵', '结界突破']
    j = 0
    # 探索单选按钮

    frameRadio = tk.Frame(window)
    frameRadio.grid(row=0, column=0, columnspan=2, pady=10)
    for i in modelName:
        tk.Radiobutton(frameRadio, text=i, variable=selectModel,
                       value=j + 1).grid(row=int(j / 5), column=int(j % 5), padx=5)
        j = j + 1
    frameText = tk.Frame(window)
    frameText.grid(row=1, column=0, columnspan=2, pady=10)
    physicalLimit = tk.StringVar()
    physicalLimit.set(0)
    limitLabel = tk.Label(frameText, text='体力限制：')
    limitText = tk.Entry(frameText, textvariable=physicalLimit, width=10)
    limitLabel.grid(row=0, column=0, sticky=tk.E)
    limitText.grid(row=0, column=1, sticky=tk.W)
    costLabel = tk.Label(frameText, text='体力消耗：')
    costText = tk.Entry(frameText, textvariable=0, state=tk.DISABLED, width=10)
    costLabel.grid(row=0, column=2, sticky=tk.E)
    costText.grid(row=0, column=3, sticky=tk.W)
    btn_start = tk.Button(window, text='开始', command=lambda: yys.start(
        logText, costText, btn_start, btn_stop, int(selectModel.get()), int(physicalLimit.get())))
    btn_start.grid(row=2, column=0, pady=10)
    btn_stop = tk.Button(window, text='暂停', command=lambda: yys.stop(
        logText, btn_start, btn_stop))
    btn_stop.grid(row=2, column=1, pady=10)
    logText.grid(row=3, column=0, columnspan=4)
    # 以上是窗口的主体
    window.mainloop()  # 结束（不停循环刷新）


if __name__ == '__main__':
    main()
