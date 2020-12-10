'''
Author: your name
Date: 2020-11-10 16:26:58
LastEditTime: 2020-12-10 14:30:31
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \YYS-master\guifuncton.py
'''
from cv2 import cv2
from PIL import ImageGrab
import numpy
import time
import random
import os
import sys
import pyautogui
import traceback
import keyboard
import tkinter as tk
import threading
import util

stopKey = 'esc'

global runFlag, log, PhysicalLimit, count, Btn_start, Btn_stop
runFlag = False
PhysicalLimit = 0
count = 0


def logMsg(logText, msg):
    logText.config(state=tk.NORMAL)
    logText.insert(tk.END, msg)
    logText.config(state=tk.DISABLED)
    logText.see(tk.END)


def changeCost(costText, cost):
    costText.config(state=tk.NORMAL)
    costText.delete(0, tk.END)
    costText.insert(0, cost)
    costText.config(state=tk.DISABLED)


def keyListener(stopKey, logText, btn_start, btn_stop):
    keyboard.wait(stopKey)
    stop(logText, btn_start, btn_stop)


def getModelName(num):
    numbers = ["单人探索", "组队御魂", "业原火", "御灵"]
    return numbers[num]


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
        listener = threading.Thread(target=keyListener, args=(
            stopKey, logText, btn_start, btn_stop))
        listener.setDaemon(True)
        listener.start()
        btn_start.config(state=tk.DISABLED)
        btn_stop.config(state=tk.NORMAL)
        msg = '%s-程序启动--可以点击Esc退出\n' % (util.getTimeFormat())
        logMsg(logText, msg)
    else:
        msg = '%s-错误，请先选择模式\n' % (util.getTimeFormat())
        logMsg(logText, msg)


def stop(logText, btn_start, btn_stop):
    global runFlag
    runFlag = False
    btn_stop.config(state=tk.DISABLED)
    btn_start.config(state=tk.NORMAL)
    msg = '%s-程序暂停\n' % (time.strftime("%H:%M:%S", time.localtime()))
    logMsg(logText, msg)

########################################################
# 单人探索


def tansuo():
    while runFlag:
        screen = util.getScreen()
        # 设定目标，开始查找
        # 进入后
        want = util.imgs['tu']
        pts = util.action.locate(screen, want, 0)
        if not len(pts) == 0:
            msg = '%s-处于地图中\n' % (util.getTimeFormat())
            logMsg(log, msg)
            want = util.imgs['left']
            pts = util.action.locate(screen, want, 0)
            if not len(pts) == 0:
                right = (854, 527)
                right = util.action.cheat(right, 10, 10)
                pyautogui.click(right)
                t = random.randint(30, 60) / 100
                time.sleep(t)
                continue
            screen = util.getScreen()
            want = util.imgs['jian']
            pts = util.action.locate(screen, want, 0)
            if not len(pts) == 0:
                msg = '%s-点击小怪\n' % (util.getTimeFormat())
                logMsg(log, msg)
                xx = util.action.cheat(pts[0], 10, 10)
                pyautogui.click(xx)
            elif not util.click(screen, 'boss'):
                for i in ['queren', 'tuichu']:
                    screen = util.getScreen()
                    if util.click(screen, i):
                        msg = '%s-退出中\n' % (util.getTimeFormat())
                        logMsg(log, msg)
                        t = random.randint(15, 30) / 100
                        time.sleep(t)
                        break
            if util.checkMan():
                count = count + 3
                changeCost(cost, count)
            if (count >= PhysicalLimit) & (PhysicalLimit != 0):
                msg = '%s-已消耗体力-%d\n' % (util.getTimeFormat(), count)
                logMsg(log, msg)
                stop(log, Btn_start, Btn_stop)
        for i in ['28', 'tansuo', 'ying', 'jiangli', 'jixu', 'jujue']:
            screen = util.getScreen()
            result = util.click(screen, i)
            if result:
                t = random.randint(10, 20) / 100
                time.sleep(t)
                continue
            else:
                continue
########################################################
# 魂土


def huntu():
    while runFlag:
        for i in ['huntutiaozhan', 'huntujiesuan', 'huntujiangli', 'huntujiesuan1', 'jiangli', 'jujue']:
            screen = util.getScreen()
            result = util.click(screen, i)
            if result:
                t = random.randint(10, 20) / 100
                time.sleep(t)
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
        for i in ['huntutiaozhan', 'huntujiesuan', 'huntujiangli', 'huntujiesuan1', 'jiangli', 'jujue']:
            screen = util.getScreen()
            result = util.click(screen, i)
            if result:
                t = random.randint(10, 20) / 100
                time.sleep(t)
                continue
            else:
                continue


########################################################
# 结界突破
# 此功能未完善


def jiejietupo():
    global runFlag, log, cost, PhysicalLimit, Btn_start, Btn_stop, count
    while runFlag:
        screen = util.getScreen()
        if util.click(screen, 'test'):
            count = count + 3
            changeCost(cost, count)
        if (count >= PhysicalLimit) & (PhysicalLimit != 0):
            msg = '%s-已消耗体力-%d\n' % (util.getTimeFormat(), count)
            logMsg(log, msg)
            stop(log, Btn_start, Btn_stop)
