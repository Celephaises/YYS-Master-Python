"""
Author: your name
Date: 2020-11-10 16:26:58
LastEditTime: 2021-01-07 12:22:50
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \YYS-master\guifuncton.py
"""
import random
import threading
import time
import tkinter as tk

import keyboard
import pyautogui

import util

# 程序暂停快捷键
stopKey = 'Esc'

global runFlag, log, PhysicalLimit, count, Btn_start, Btn_stop, cost
# 程序运行标志
runFlag = False
# 体力初始默认值
PhysicalLimit = 0
# 体力消耗统计
count = 0


# 打印消息到前端


def logMsg(logText, msg):
    logText.config(state=tk.NORMAL)
    logText.insert(tk.END, msg)
    logText.config(state=tk.DISABLED)
    logText.see(tk.END)


# 变更体力消耗数值


def changeCost(costText, cost):
    costText.config(state=tk.NORMAL)
    costText.delete(0, tk.END)
    costText.insert(0, cost)
    costText.config(state=tk.DISABLED)


# 键盘监听器


def keyListener(logText, btn_start, btn_stop):
    keyboard.wait('Esc')
    stop(logText, btn_start, btn_stop)


# 程序启动


def start(logText, costText, btn_start, btn_stop, selectModel, physicalLimit):
    mode = [0, tansuo, huntu, yeyuanhuo, yuling, jiejietupo]
    if selectModel != 0:
        global runFlag, log, cost, PhysicalLimit, Btn_start, Btn_stop, count
        log = logText
        cost = costText
        Btn_start = btn_start
        Btn_stop = btn_stop
        runFlag = True
        if physicalLimit != 0:
            PhysicalLimit = physicalLimit
        comand = mode[selectModel]
        worker = threading.Thread(target=comand)
        worker.setDaemon(True)
        worker.start()
        listener = threading.Thread(
            target=keyListener, args=(logText, btn_start, btn_stop))
        listener.setDaemon(True)
        listener.start()
        btn_start.config(state=tk.DISABLED)
        btn_stop.config(state=tk.NORMAL)
        msg = '%s-程序启动--可以点击Esc退出\n' % (util.getTimeFormat())
        logMsg(logText, msg)
    else:
        msg = '%s-错误，请先选择模式\n' % (util.getTimeFormat())
        logMsg(logText, msg)


# 程序暂停


def stop(logText, btn_start, btn_stop):
    global runFlag
    runFlag = False
    btn_stop.config(state=tk.DISABLED)
    btn_start.config(state=tk.NORMAL)
    msg = '%s-程序暂停\n' % (util.getTimeFormat())
    logMsg(logText, msg)


########################################################
# 单人探索


def tansuo():
    global count, PhysicalLimit
    while runFlag:
        # 设定目标，开始查找
        # 进入后
        want = util.imgs['tu']
        pts = util.action.locate(util.getScreen(), want, 0)
        if not len(pts) == 0:
            msg = '%s-处于地图中\n' % (util.getTimeFormat())
            logMsg(log, msg)
            want = util.imgs['left']
            pts = util.action.locate(util.getScreen(), want, 0)
            if not len(pts) == 0:
                right = (854, 527)
                right = util.action.cheat(right, 10, 10)
                pyautogui.click(right)
                time.sleep(random.randint(30, 60) / 100)
                continue
            want = util.imgs['jian']
            pts = util.action.locate(util.getScreen(), want, 0)
            if len(pts) >= 1:
                msg = '%s-点击小怪\n' % (util.getTimeFormat())
                logMsg(log, msg)
                xx = util.action.cheat(pts[0], 10, 10)
                pyautogui.click(xx)
            else:
                for i in ['queren', 'tuichu']:
                    if util.click(i):
                        msg = '%s-退出中\n' % (util.getTimeFormat())
                        logMsg(log, msg)
                        time.sleep(random.randint(15, 30) / 100)
                        break
            if util.checkMan():
                count = count + 3
                changeCost(cost, count)
            if (count >= PhysicalLimit) & (PhysicalLimit != 0):
                msg = '%s-已消耗体力-%d\n' % (util.getTimeFormat(), count)
                logMsg(log, msg)
                stop(log, Btn_start, Btn_stop)
        want = util.imgs['jjtpman']
        pts = util.action.locate(util.getScreen(), want, 0)
        if len(pts) >= 1:
            print('结界突破满')
            util.click('28guanbi')
            time.sleep(random.randint(50, 80) / 100)
            util.click('jjtpkaishi')
            while True:
                if util.click('jjtpjieshu'):
                    while not util.click('jjtpguanbi'):
                        pass
                    break
                elif util.click('shuaxinqueren'):
                    pass
                elif util.click('jjtpjingong'):
                    pass
                elif util.click('jjtp'):
                    pass
                else:
                    util.click('jjtpshuaxin')
                for i in ['jjtpjiesuan', 'jjtpjiesuan1', 'jjtpjiesuan2', 'jjtpshibai', 'jujue']:
                    if util.click(i):
                        time.sleep(random.randint(10, 20) / 100)
                        continue
                    else:
                        continue
        for i in ['28', 'tansuo', 'ying', 'jiangli', 'jixu', 'jujue', 'yuhunqueren']:
            if util.click(i):
                time.sleep(random.randint(10, 20) / 100)
                continue
            else:
                continue


########################################################
# 魂土


def huntu():
    while runFlag:
        for i in ['huntutiaozhan', 'huntujiesuan', 'huntujiangli', 'huntujiesuan1', 'jiangli', 'jujue']:
            if util.click(i):
                time.sleep(random.randint(10, 20) / 100)
                continue
            else:
                continue


########################################################
# 业原火
# 此功能未完善


def yeyuanhuo():
    while runFlag:
        for i in ['yeyuanhuotiaozhan', 'yeyuanhuojiesuan', 'yeyuanhuojiangli', 'yeyuanhuojiesuan1', 'jiangli', 'jujue']:
            screen = util.getScreen()
            result = util.click(screen, i)
            if result:
                t = random.randint(10, 20) / 100
                time.sleep(t)
                continue
            else:
                continue


########################################################
# 御灵
# 此功能未完善


def yuling():
    while runFlag:
        for i in ['yulintiaozhan', 'huntujiesuan', 'huntujiangli', 'huntujiesuan1', 'jiangli', 'jujue']:
            screen = util.getScreen()
            if util.click(screen, i):
                t = random.randint(10, 20) / 100
                time.sleep(t)
                continue
            else:
                continue


########################################################
# 结界突破
# 此功能未完善


def jiejietupo():
    global runFlag, log, Btn_start, Btn_stop, count
    while runFlag:
        if util.click('jjtpjieshu'):
            stop(log, Btn_start, Btn_stop)
        elif util.click('shuaxinqueren'):
            pass
        elif util.click('jjtpjingong'):
            pass
        elif util.click('jjtp'):
            pass
        else:
            util.click('jjtpshuaxin')
        for i in ['jjtpjiesuan', 'jjtpjiesuan1', 'jjtpjiesuan2', 'jujue']:
            if util.click(i):
                time.sleep(random.randint(10, 20) / 100)
                continue
            else:
                continue
