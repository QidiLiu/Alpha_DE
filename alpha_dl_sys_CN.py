#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"Video&Sub download helper"

__author__ = 'QidiLiu'

import tkinter as tk
import os
import re

# Ref.
# https://zhuanlan.zhihu.com/p/27718783
# https://github.com/ytdl-org/youtube-dl

ft_1 = ('Microsoft YaHei', 10, 'bold')
with open('proxy.txt', 'r') as f:
    proxy = f.read()

if __name__ == "__main__":
    root = tk.Tk()
    root.title('阿尔法小分队视频下载器（代理版）')
    root.iconbitmap('Alpha.ico')

    fr_1 = tk.Frame(root)
    fr_1.grid(row=0, column=0)

    link_entry = tk.Entry(fr_1, width=50)
    link_entry.grid(row=0, column=0)
    wait_label = tk.Label(fr_1, text='下载中...', font=ft_1)

    def recall_ytbdl():
        link = link_entry.get()
        link_entry.delete(0, tk.END)
        link_entry.grid_forget()
        wait_label.grid(row=0, column=0)
        root.update()
        os.system('.\\youtube-dl --proxy 127.0.0.1:' + proxy + ' --all-subs -f bestvideo+bestaudio -o "/downloads/%(title)s.%(ext)s" ' + link)
        wait_label.grid_forget()
        link_entry.grid(row=0, column=0)
    
    link_entry.bind('<Return>', lambda n:recall_ytbdl())

    def convert2mp4():
        os.chdir('./downloads')
        for f in os.listdir('.'):
            if f.split('.')[-1] == 'webm' or f.split('.')[-1] == 'mkv':
                file_name = f.split(f.split('.')[-1])[0]
                os.system(str(f'ffmpeg -i "{f}" "{file_name}"mp4'))
                os.remove(f)
            elif f.split('.')[-1] == 'vtt':
                file_name = f.split(f.split('.')[-1])[0]
                os.system(str(f'ffmpeg -i "{f}" "{file_name}"ass'))
                #os.remove(f)
    convert_button = tk.Button(fr_1, text='开始转码', font=ft_1, command=convert2mp4)
    convert_button.grid(row=0, column=1)

    root.mainloop()