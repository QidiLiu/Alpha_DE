#!/bin/bash
# -*- coding: utf-8 -*-

"方便打轴时自动为后续翻译留中文位置"

__author__ = 'QidiLiu'

from tkinter import filedialog
from tkinter.messagebox import showinfo
from re import match
from os import _exit

ass_file = filedialog.askopenfile(title='请选择待处理字幕文件', mode ='r', filetypes =[('ass格式字幕文件', '*.ass')])
if ass_file is not None:
    print(ass_file.name)
    with open(ass_file.name, 'r', encoding='UTF-8') as file_read:
        lines = file_read.readlines()
    with open(ass_file.name, 'w', encoding='UTF-8') as file_write:
        for line in lines:
            if match('Dialogue:', line) is not None:
                new_line = ''.join(list(line)[:34])+'Default,,0,0,0,,'
                line = line+new_line+'\n'
            file_write.write(line)
    showinfo('顺便一提，你真好看', '处理成功！！！')
_exit(0)
