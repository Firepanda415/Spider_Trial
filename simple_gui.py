# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 09:32:43 2017

@author: hazhou
"""

import tkinter
from tkinter import ttk
import jiandan
import newest_page

root = tkinter.Tk()
##create the main lable for the GUI
#MainLabel = tkinter.Label(root, text = 'Jiandan Pic Grabber', font = 
#                          'Times 16')
#MainLabel.pack()

##Create a frame
#frame = tkinter.Frame(root)
#frame.pack()

##Create a button for quitting
#button1 = tkinter.Button(frame, text = 'Quit', fg = 'red', command = frame.quit)
#button1.pack(side = tkinter.BOTTOM)
#
##Create a button for starting grabbing
#button2 = tkinter.Button(frame, text = 'Start', command = jiandan.grab(194,190))
#button2.pack(side = tkinter.TOP)




#Use ttk instead of tkinter to make GUI more beautiful
#Use grid to control the layout more easily
frame = ttk.Frame(root,padding=20) #padding = width(pixels) of the borders
frame.grid()

MainLabel = ttk.Label(frame, text = 'Jiandan Pic Grabber', font = 'Times 16')
MainLabel.grid(row=0,column=0,columnspan=3,sticky='n')

newest = newest_page.get_newest()
newest_indicator = ttk.Label(frame, text = 'The newest page avaliable is ' + 
                             str(newest), font = 'Times 14')
newest_indicator.grid(row = 1, column = 0, columnspan=3,sticky='n')

start_page = ttk.Entry(frame, width=15)
start_page.grid(row=2,column=1,columnspan = 2)

ending_page = ttk.Entry(frame, width=15)
ending_page.grid(row=3,column=1,columnspan = 2)

pic_num = ttk.Entry(frame, width=15)
pic_num.grid(row=4,column=1,columnspan = 2)

sp_label = ttk.Label(frame, text = 'Start Page', font = 'Times 10')
sp_label.grid(row=2,column=0)

ep_label = ttk.Label(frame, text = 'End Page', font = 'Times 10')
ep_label.grid(row=3,column=0)

def get(string):
    if string == '':
        lim = False
        pic = 0
        return lim, pic
    else:
        lim = True
        pic = int(pic_num.get())
        return lim, pic
    
pic_label = ttk.Label(frame, text = 'Pic Number', font = 'Times 10')
pic_label.grid(row=4,column=0)

s_button = ttk.Button(frame, text='Start', command=lambda: jiandan.grab(start_page.get(),
                                                                        ending_page.get(),get(pic_num.get())[0],
                                                                        get(pic_num.get())[1]))
s_button.grid(row=5,column=0,columnspan = 2)

q_button = ttk.Button(frame, text='Quit')
q_button.grid(row=5,column=2)
q_button['command'] = lambda: root.destroy()

root.mainloop()