# -*- coding: utf-8 -*-

"方便打轴时自动为后续翻译留中文位置"

__author__ = 'QidiLiu'

from tkinter import Tk, Button, filedialog
from tkinter.messagebox import showinfo
from re import match
from os import _exit

root = Tk()
root.title('空白行打轴器 —— 阿尔法小分队德语组专用')
root.geometry('500x260')

def find_ass():
    find_button['state'] = 'disabled'
    ass_file = filedialog.askopenfile(title='请选择待处理字幕文件', mode ='r', filetypes =[('ass格式字幕文件', '*.ass')])
    if ass_file is not None: 
        print(ass_file.name)
        with open(ass_file.name, 'r', encoding='UTF-8') as file_read:
            lines = file_read.readlines()
        with open(ass_file.name, 'w', encoding='UTF-8') as file_write:
            for line in lines:
                if match('Dialogue:', line) is not None:
                    new_line = ''.join(list(line)[:41])+',,0,0,0,,'
                    line = line+new_line+'\n'
                file_write.write(line)
        showinfo('处理成功！！！', '顺便一提，你真好看')
    _exit(0)

find_button = Button(root, text='憋说话，点我！！！', command=find_ass, font=('Helvetica', 30, 'bold'), width=18, height=4)
find_button.place(x=250, y=130, anchor='center')

root.mainloop()
