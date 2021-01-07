# coding=utf-8
import random
import time

import cv2
import pyautogui
from PIL import ImageGrab

import action

# 读取文件 精度控制   显示名字
imgs = action.load_imgs()
pyautogui.PAUSE = 0.1


def checkMan():
    screen = getScreen()
    want = imgs['man']
    pts = action.locate(screen, want, 0)
    if len(pts) >= 2:
        print('更换狗粮')
        want = imgs['diban']
        pts = action.locate(screen, want, 0)
        if len(pts) >= 1:
            size = want[0].shape
            h, w, ___ = size
            xy = action.cheat(pts[0], w, h - 10)
            pyautogui.doubleClick(xy)
            time.sleep(2)
            screen = getScreen()
            upleft = (500, 0)
            downright = (1200, 500)
            a, b = upleft
            c, d = downright
            screen = screen[b:d, a:c]
            want = imgs['man']
            man = action.locate(screen, want, 0)
            while len(man) >= 1:
                screen = getScreen()
                if click(screen, 'quanbu'):
                    t = random.randint(50, 80) / 100
                    time.sleep(t)
                    screen = getScreen()
                    if click(screen, 'ncard'):
                        t = random.randint(50, 80) / 100
                        time.sleep(t)
                    screen = getScreen()
                want = imgs['ncard']
                ncard = action.locate(screen, want, 0)
                if len(ncard) >= 1:
                    while len(man) >= 1:
                        man = getManXy()
                        screen = getScreen()
                        want = imgs['gouliang']
                        gouliang = action.locate(screen, want, 0)
                        if len(gouliang) >= 2:
                            gouliangxy = action.cheat(
                                gouliang[random.randint(0, len(gouliang) - 1)], w, h)
                            if len(man) >= 1:
                                pyautogui.mouseDown(
                                    gouliangxy[0] + 10, gouliangxy[1] + 10)
                                pyautogui.dragTo(man[0][0], man[0][1] + 40, 0.5)
                            screen = getScreen()
                            man = getManXy()
                            action.locate(screen, want, 0)
                        else:
                            screen = getScreen()
                            want = imgs['gundongtiao']
                            pts = action.locate(screen, want, 0)
                            if len(pts) >= 1:
                                xy = action.cheat(pts[0], w, h)
                                pyautogui.mouseDown(xy)
                                pyautogui.dragTo(xy[0] + 30, xy[1], 0.5)
                man = getManXy()
    screen = getScreen()
    return click(screen, 'zhunbei')


def getScreen():
    screen = ImageGrab.grab()
    screen.save('screen.jpg')
    screen = cv2.cv2.imread('screen.jpg')

    # 截屏，并裁剪以加速
    upleft = (0, 0)
    downright = (1358, 768)

    a, b = upleft
    c, d = downright
    screen = screen[b:d, a:c]
    return screen


def click(s, screen=getScreen()):
    want = imgs[s]
    size = want[0].shape
    h, w, ___ = size
    pts = action.locate(screen, want, 0)
    if len(pts) >= 1:
        xy = action.cheat(pts[0], w, h)
        pyautogui.click(xy)
        return True
    return False


def getManXy():
    screen = ImageGrab.grab()
    screen.save('screen.jpg')
    screen = cv2.cv2.imread('screen.jpg')
    upleft = (500, 0)
    downright = (1200, 500)
    a, b = upleft
    c, d = downright
    screen = screen[b:d, a:c]
    manxy = []
    for i in ['man1', 'man']:
        want = imgs[i]
        pts = action.locate(screen, want, 0)
        if len(pts) >= 1:
            xy = action.cheat(pts[0], 5, 5)
            xy[0] = xy[0] + 500
            manxy.append(xy)
    return manxy


def getTimeFormat():
    return time.strftime("%H:%M:%S", time.localtime())
