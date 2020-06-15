#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"基于ffmpeg的影音转码、压制工具"

__author__ = 'QidiLiu'

import tkinter as tk
from tkinter import filedialog
from os import system, listdir, remove, _exit
from shutil import copy
from threading import Thread

ft_1 = ('Microsoft YaHei', 12)
ft_2 = ('Microsoft YaHei', 20, 'bold')
n_threads = 1

root = tk.Tk()
root.title('小刘影音工具箱')
VIDEO_FILE = None
SUB_FILE = None
SUB_EXT = None

def check():
    if VIDEO_FILE is not None and SUB_FILE is not None:
        start_button.grid(row=0, column=2, rowspan=2)

def video_select():
    global VIDEO_FILE
    VIDEO_FILE = filedialog.askopenfile(title='请选择视频文件', mode ='r', filetypes =[('mkv/mp4/avi格式视频文件', '*.mkv; *.mp4; *.avi')])
    if VIDEO_FILE is not None:
        video_var.set(VIDEO_FILE.name)
        check()

input_video_bt = tk.Button(root, text='选择视频', font=ft_1, command=video_select, width=10)
input_video_bt.grid(row=0, column=0)
video_var = tk.StringVar()
video_var.set('      暂未选择视频      ')
input_video_lb = tk.Label(root, textvariable=video_var, font=ft_1)
input_video_lb.grid(row=0, column=1)

def subtitle_select():
    global SUB_FILE, SUB_EXT
    SUB_FILE = filedialog.askopenfile(title='请选择ass字幕文件', mode='r', filetypes=[('ass/srt/vtt格式字幕文件', '*.ass; *.srt; *.vtt')])
    
    if SUB_FILE is not None:
        subtitle_var.set(SUB_FILE.name)
        SUB_EXT = SUB_FILE.name.split('.')[-1]
        for f in listdir('.'):
            ext = f.split('.')[-1]
            if ext == 'ass' or ext == 'srt' or ext == 'vtt':
                remove(f)
        copy(SUB_FILE.name, 'sub.'+SUB_EXT)
        check()
    
input_subtitle_bt = tk.Button(root, text='选择字幕', font=ft_1, command=subtitle_select, width=10)
input_subtitle_bt.grid(row=1, column=0)
subtitle_var = tk.StringVar()
subtitle_var.set('      暂未选择字幕      ')
input_subtitle_lb = tk.Label(root, textvariable=subtitle_var, font=ft_1)
input_subtitle_lb.grid(row=1, column=1)

def thread_job(output_file):
    system(str(f'.\\ffmpeg -i "{VIDEO_FILE.name}" -vf subtitles="sub.{SUB_EXT}" "{output_file}"'))

def start():
    video_name = VIDEO_FILE.name.split('/')[-1].split('.'+VIDEO_FILE.name.split('.')[-1])[0]
    output_file = filedialog.asksaveasfilename(title='请选择输出视频保存路径&名称', filetypes=[('mp4视频', '*.mp4')], defaultextension='mp4', initialfile=str(f'输出_{video_name}.mp4'))
    Thread(target=thread_job(output_file)).start()

start_button = tk.Button(root, text='确认无误\n开始压制', font=ft_2, command=start)

def close_window():
    for f in listdir('.'):
        ext = f.split('.')[-1]
        if ext == 'ass' or ext == 'srt' or ext == 'vtt':
            remove(f)
    _exit(0)

root.protocol('WM_DELETE_WINDOW', close_window)

root.mainloop()
