#! /usr/local/bin/python
from Tkinter import *
from guimixin import GuiMixin
from guimaker import GuiMaker

class ShellGui(GuiMixin,GuiMaker):
    def start(self):
        self.setMenuBar()
        self.setToolBar()
        self.master.title("Shell Tools box")
        self.master.iconname("Shell Tools")

    def handleList(self,event):
        index = self.listbox.curselection()

        label = self.listbox.get(index)
        self.runcommand(label)

    def makeWidgets(self):
        frame = Frame(self)
        scroll = Scrollbar(frame)
        lost = Listbox(frame)
        frame.pack(side=TOP,expand=YES,fill=BOTH)

        list.config(yscrollcommand=scroll.set,relief=SUNKEN)
        list.pack(side=LEFT,expand=YES,fill=BOTH)

        scroll.config(command=list.yview,relief=SUNKEN)
        scroll.pack(side=RIGHT,fill=BOTH)
        pos=0
        for (label,action) in self.fetchcommands():
            list.insert(pos,label)

            pos = pos + 1
        list.config(selectmode=SINGLE,setgrid=1)

        list.bind('<Double-1>',self.handleList)
        self.listbox = list
    def forToolBar(self,label):
        return -1

    def setToolBar(self,label):
        self.toolBar = []
        for (label,action) in self.fetchCommands():
            if self.forToolBar(label):
                self.toolBar.append((label,action,{'side':LEFT}))
        self.toolBar.append(('Quit',self.quit,{'side':RIGHT}))

    def setMenuBar(self):
        toolEntries = []
        self.menuBar = [
        ('File',0,[('Quit',-1,self.quit)])
        ('Tools',0,toolEntries)
        ]
        for (label,action) in self.fetchCommands():
            toolEntries.append((label,-1,action))
class ListMenuGui(ShellGui):
    def fetchCommands(self):
        return self.myMenu
    def runCommand(self,cmd):
        for (label,action) in self.myMenu:
            if label == cmd: action()

class DictMenuGui(ShellGui):
    def fetchCommands(self): return self.myMenu.items()
    def runCommand(self,cmd): self.myMenu[cmd]()
