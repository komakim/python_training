from Tkinter import *

def frame(self,side):
    widget = Frame(root)
    widget.pack(side=side,expand=YES,fill=BOTH)
    return widget

def label(root,side,text):
    widget = Label(root,text=text,relief = RIDGE)
    widget.pack(side=side,expand=YES,fill=BOTH)
    return widget

def button(root,side,text,command):
    widget = Button(root,text=text,command=command)
    widget.pack(side=side,expand=YES,fill=BOTH)
    return widget
     
