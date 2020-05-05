#!/usr/bin/python
# -*- coding: utf-8 -*-

"为youtube-dl加了个UI操作界面"

# The main function of this program is from youtube-dl.
# Github link of youtube-dl: https://github.com/ytdl-org/youtube-dl

__author__ = 'QidiLiu'

from tkinter import Tk, Entry, Button, LEFT, Label
from os import _exit, system

root = Tk()
root.title('请将视频链接填入下框，然后点下载')

link_entry = Entry(root, width=50)
link_entry.pack(side=LEFT)

def recall_ytbdl():
    wait_label.pack()
    link = link_entry.get()
    link_entry.destroy()
    conform_button.destroy()
    root.update()
    system('.\\youtube-dl --id --cache-dir DIR -f bestvideo+bestaudio ' + link)
    system('explorer .')
    _exit(0)

conform_button = Button(root, text='下载', command=recall_ytbdl)
conform_button.pack()
link_entry.bind('<Return>', lambda n:recall_ytbdl())

wait_label = Label(root, text='正在下载，请稍候...')

root.mainloop()