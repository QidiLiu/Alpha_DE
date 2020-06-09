#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"Help user copy modified words with hot keys"

__author__ = 'QidiLiu'

import keyboard
import pyautogui
import pyperclip
import time

curse_1 = '（机器轴）'
curse_2 = '（内嵌字幕 只需翻中）'
curse_3 = '（人工轴）'
curse_4 = ' '

def paste(curse):
    pyperclip.copy(curse)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.2)

if __name__ == "__main__":
    keyboard.add_hotkey('ctrl+f1', paste, args=(curse_1,))
    keyboard.add_hotkey('ctrl+f2', paste, args=(curse_2,))
    keyboard.add_hotkey('ctrl+f3', paste, args=(curse_3,))
    keyboard.add_hotkey('ctrl+f4', paste, args=(curse_4,))

    keyboard.wait()
