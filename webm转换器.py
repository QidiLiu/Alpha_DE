# -*- coding: utf-8 -*-

"将webm格式视频转为mp4格式视频"

__author__ = 'QidiLiu'

from tkinter import filedialog
from os import _exit, system, chdir

webm_file = filedialog.askopenfile(title='请选择待处理视频文件', mode ='r', filetypes =[('webm格式视频文件', '*.webm')]).name
chdir(webm_file.split(webm_file.split('/')[-1])[0])
file_name = webm_file.split('/')[-1].split('.webm')[0]
system('copy ' + webm_file.split('/')[-1] + ' ' + file_name + '.mp4')
_exit(0)