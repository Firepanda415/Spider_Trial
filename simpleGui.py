# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 09:32:43 2017

@author: hazhou
"""

import tkinter
import jiandan

root = tkinter.Tk()
MainLabel = tkinter.Label(root, text = 'Jiandan Pic Grabber', font = 
                          'Times 16')
MainLabel.pack()

frame = tkinter.Frame(root)
frame.pack()

button1 = tkinter.Button(frame, text = 'Quit', fg = 'red', command = frame.quit)
button1.pack(side = tkinter.BOTTOM)

button2 = tkinter.Button(frame, text = 'Start', command = jiandan.grab)
button2.pack(side = tkinter.TOP)

def dostuff():
    jiandan.grab()

root.mainloop()
root.destroy()