# -*- coding: utf-8 -*-

"提取.ass字幕文件中所有字幕文字并输出txt格式文档"

__author__ = 'QidiLiu'

from tkinter import filedialog
from re import match
from os import _exit

TEXT = ''

ass_file = filedialog.askopenfile(title='请选择待处理字幕文件', mode ='r', filetypes =[('ass格式字幕文件', '*.ass')])
if ass_file is not None:
    with open(ass_file.name, 'r', encoding='UTF-8') as file_read:
        lines = file_read.readlines()
    with open(ass_file.name.split(ass_file.name.split('/')[-1])[0]+'text_'+ass_file.name.split('/')[-1].split('.')[0]+'.txt', 'w', encoding='UTF-8') as file_write:
        for line in lines:
            if match('Dialogue:', line) is not None:
                TEXT = ''.join(list(line.strip('\n'))[54:])
            file_write.write(TEXT)

_exit(0)
