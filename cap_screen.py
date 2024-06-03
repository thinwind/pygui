# -*- coding: utf-8 -*-
'''
@Time   :  2024-6月-03 14:56
@Author :  Shang Yehua
@Email  :  niceshang@outlook.com
@Desc   :  
        屏幕截图
'''
import pyautogui

x= 2714
y = 1604
# pyautogui.moveTo(2714,1604,duration=1)  
for i in range(100):
    pyautogui.sleep(1)
    # 在指定位置按下鼠标左键import pyautogui
    # 在指定的位置按下鼠标左键
    pyautogui.click(x, y)
    # 休眠1秒
    # 截图,保存到指定路径
    pyautogui.screenshot(f'C:/Users/nices/tmp/pygui/pic_{i}.png')
 