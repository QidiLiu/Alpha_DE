# -*- coding: utf-8 -*-

"利用谷歌翻译自动生成中文字幕轴 —— 实验阶段"

__author__ = 'QidiLiu'

from tkinter import Tk, Button, filedialog
from re import match
from googletrans import Translator

translator = Translator()

root = Tk()
root.title('自动翻译轴生成器')
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
                    new_line = ''.join(list(line)[:50])
                    original_text = ''.join(list(line)[50:])
                    print(original_text)
                    zh = translator.translate(original_text, dest='zh-CN').text
                    print(zh)
                    line = line+new_line+zh+'\n'
                file_write.write(line)


find_button = Button(root, text='憋说话，点我！！！', command=find_ass, font=('Helvetica', 30, 'bold'), width=18, height=4)
find_button.place(x=250, y=130, anchor='center')

root.mainloop()
