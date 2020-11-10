'''
Author: your name
Date: 2020-11-10 10:43:46
LastEditTime: 2020-11-10 17:31:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \YYS-master\gui.py
'''
import tkinter as tk
import time
import yys

window = tk.Tk()  # 创建窗口
window.title("阴阳师助手")  # 窗口标题
window.geometry('400x200')  # 窗口大小，小写字母x
window.resizable(0, 0)  # 设置窗口大小不可变

# 副本模式
selectModel = tk.StringVar()
selectModel.set(0)

logText = tk.Text(window, height=10, width=80, state=tk.DISABLED)
logText.grid(row=2, column=0, columnspan=4)

# 探索单选按钮
tk.Radiobutton(window, text='单人探索', variable=selectModel, value='1', command=lambda: yys.logMsg(
    logText, '%s-单人探索模式\n' % (time.strftime("%H:%M:%S", time.localtime())))).grid(row=0, column=0)

tk.Radiobutton(window, text='组队御魂', variable=selectModel, value='2', command=lambda: yys.logMsg(
    logText, '%s-组队御魂模式\n' % (time.strftime("%H:%M:%S", time.localtime())))).grid(row=0, column=1)

btn_start = tk.Button(window, text='开始', command=lambda: yys.start(
    logText, btn_start, btn_stop, int(selectModel.get())))
btn_start.grid(row=1, column=0)
btn_stop = tk.Button(window, text='暂停', command=lambda: yys.stop(
    logText, btn_start, btn_stop))
btn_stop.grid(row=1, column=1)


# 以上是窗口的主体
window.mainloop()  # 结束（不停循环刷新）
