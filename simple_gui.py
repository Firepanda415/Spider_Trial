# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 09:32:43 2017

@author: hazhou
"""

import tkinter
from tkinter import *
import jiandan
import newest_page

#Create an warn object that could create a warning window
class warn(object):
    def __init__(self, message):
        self.message = message
        
    def ml(self, root, r, c, cs):
        MainLabel = ttk.Label(root, text = self.message)
        MainLabel.grid(row = r, column = c, columnspan = cs)
        
    def q(self, root, txt, r, c):
        q_button = ttk.Button(root, text=txt)
        q_button.grid(row=r,column=c)
        q_button['command'] = lambda: root.destroy()
        
    def tk_instance(self):
        root = tkinter.Tk()
        self.ml(root, 0, 0, 3)
        self.q(root, 'OK', 1, 0)
        root.mainloop()

#Expand the warn object so that it could return a boolean value        
class proceed(warn):
    return_value = True
    def __init__(self, message):
        self.message = message
        
    def go_on(self, root, txt, r, c):
        go_button = ttk.Button(root, text=txt)
        go_button.grid(row=r,column=c)
        go_button['command'] = lambda: root.destroy()
        
    def return_false(self, root):
        root.destroy()
        self.return_value = False
        
    def super_q(self, root, txt, r, c):
        q_button = ttk.Button(root, text=txt)
        q_button.grid(row=r,column=c)
        q_button['command'] = lambda: self.return_false(root)
    
    def tk_proceed(self):
        root = tkinter.Tk()
        self.ml(root, 0, 0, 3)
        self.go_on(root, 'Go on', 1, 0)
        self.super_q(root, 'Quit', 2, 0)
        root.mainloop()

#Ask for user's consent to proceed
def go_on():
    ask = proceed('Recommended for age of 18 or plus. Do you wish to proceed?')
    ask.tk_proceed()
    return ask.return_value

#The main root of the pic grabber
def main():
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
    
    var = BooleanVar()
    pic_num_ind = ttk.Checkbutton(frame, text = 'Assign Picture Quantity', variable = var)
    pic_num_ind.grid(row=4, column=1, columnspan=1)
    
    pic_num = ttk.Entry(frame, width=15)
    pic_num.grid(row=5,column=1,columnspan = 2)
    
    sp_label = ttk.Label(frame, text = 'Start Page', font = 'Times 10')
    sp_label.grid(row=2,column=0)
    
    ep_label = ttk.Label(frame, text = 'End Page', font = 'Times 10')
    ep_label.grid(row=3,column=0)
        
    pic_label = ttk.Label(frame, text = 'Pic Number', font = 'Times 10')
    pic_label.grid(row=5,column=0)
     
    #Check if the starting page and the ending page are illegal
    def check_run():
        try: 
            num_start = int(start_page.get())
            num_end = int(ending_page.get())
        except: 
            warn('Please enter an integer for the starting and ending page!').tk_instance()
            return False
        if num_start <= 0 or num_start > newest:
            warn('Starting page exceeding page limit').tk_instance()
            return False
        elif num_end <= 0 or num_end > newest:
            warn('Ending page exceeding page limit').tk_instance()
            return False
        return True
    #Grab the pictures unless the pic_num input is illegal
    def get_num(bool):
        if check_run(): 
            if bool:
                try: 
                    num = int(pic_num.get())
                    jiandan.grab(start_page.get(),ending_page.get(), var.get(),num)
                except:
                    warn('Please enter an integer for pic quantity!').tk_instance()
            else:
                jiandan.grab(start_page.get(),ending_page.get(), var.get(),0)
                
    
    s_button = ttk.Button(frame, text='Start', command=lambda: get_num(var.get()))
    s_button.grid(row=6,column=0,columnspan = 2)
    
    q_button = ttk.Button(frame, text='Quit')
    q_button.grid(row=6,column=2)
    q_button['command'] = lambda: root.destroy()
    
    root.mainloop()

if go_on():
    main()