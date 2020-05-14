# -*- coding: utf-8 -*-

"利用谷歌翻译自动生成中文字幕轴 —— 实验阶段"

__author__ = 'QidiLiu'

from tkinter import filedialog
from tkinter.messagebox import showinfo
from re import match
from googletrans import Translator
from os import _exit

translator = Translator()

ass_file = filedialog.askopenfile(title='请选择待处理字幕文件', mode ='r', filetypes =[('ass格式字幕文件', '*.ass')])
if ass_file is not None:
    print(ass_file.name)
    with open(ass_file.name, 'r', encoding='UTF-8') as file_read:
        lines = file_read.readlines()
    with open(ass_file.name, 'w', encoding='UTF-8') as file_write:
        for line in lines:
            if match('Dialogue:', line) is not None:
                new_line = ''.join(list(line)[:34])+'Default,,0,0,0,,'
                original_text = ''.join(list(line)[55:])
                print(original_text)
                zh = translator.translate(original_text, dest='zh-CN').text
                print(zh)
                line = line+new_line+zh+'\n'
            file_write.write(line)
    showinfo('顺便一提，你真好看', '处理成功！！！')
_exit(0)
