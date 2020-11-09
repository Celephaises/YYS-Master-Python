# coding=utf-8
from cv2 import cv2
from PIL import ImageGrab
import numpy
import time
import random
import os
import sys
import pyautogui
import traceback
import action
import util
import _thread

# 读取文件 精度控制   显示名字
imgs = action.load_imgs()
pyautogui.PAUSE = 0.1
stopKey='esc'

start_time = time.time()
print('程序启动，现在时间', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )


# 以上启动，载入设置
##########################################################

def log(f):
    def wrap(*agrs, **kwagrs):
        try:
            ans = f(*agrs, **kwagrs)
            return ans
        except:
            traceback.print_exc()
            time.sleep(60)

    return wrap


@log
def select_mode():
    print('''\n菜单：  鼠标移动到最右侧中止并返回菜单页面,
        1 单刷探索副本
        2 组队魂土
        ''')
    action.alarm(1)
    raw = input("选择功能模式：")
    index = int(raw)

    mode = [0,tansuo, huntu]
    comand = mode[index]
    comand()

########################################################
# 单人探索


def tansuo():
    while True:  # 直到取消，或者出错
        if pyautogui.position()[0] >= pyautogui.size()[0] * 0.98:
            select_mode()
        screen = util.getScreen()
        # 设定目标，开始查找
        # 进入后
        want = imgs['tu']
        size = want[0].shape
        h, w, ___ = size
        target = screen
        pts = action.locate(target, want, 0)
        if not len(pts) == 0:
            print('正在地图中')
            want = imgs['left']
            target = screen
            pts = action.locate(target, want, 0)
            if not len(pts) == 0:
                right = (854, 527)
                right = action.cheat(right, 10, 10)
                pyautogui.click(right)
                t = random.randint(30, 60) / 100
                time.sleep(t)
                continue
            screen = util.getScreen()
            want = imgs['jian']
            target = screen
            pts = action.locate(target, want, 0)
            if not len(pts) == 0:
                print('点击小怪')
                xx = action.cheat(pts[0], 10, 10)
                pyautogui.click(xx)
            else:
                for i in ['queren', 'tuichu']:
                    screen = util.getScreen()
                    if util.click(screen, i):
                        print('退出中')
                        t = random.randint(20, 50) / 100
                        time.sleep(t)
                        break
            util.checkMan()
        for i in ['28', 'tansuo', 'ying', 'jiangli', 'jixu', 'jujue']:
            screen = util.getScreen()
            result = util.click(screen, i)
            if result:
                t = random.randint(20, 40) / 100
                time.sleep(t)
                continue
            else:
                continue

########################################################
# 魂土


def huntu():
    _thread.start_new_thread(util.keyListener, (stopKey,))
    while util.runFlag:
        if pyautogui.position()[0] >= pyautogui.size()[0] * 0.98:
            select_mode()
        for i in ['huntutiaozhan', 'huntujiesuan', 'huntujiangli', 'huntujiesuan1', 'jiangli', 'jujue']:
            screen = util.getScreen()
            result = util.click(screen, i)
            if result:
                t = random.randint(10, 20) / 100
                time.sleep(t)
                continue
            else:
                continue
    util.runFlag = True
    select_mode()


if __name__ == '__main__':
    select_mode()
