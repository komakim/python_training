#!/usr/local/bin/python

from Tkinter import *
from Dialog import Dialog

class Hello(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.pack()
        self.createWidgets()
        self.master.title("Buttons and Menus")
        self.master.iconname("tkpython")

    def createWidgets(self):
        self.makeMenuBar()
        Label(self,text='Hello menu/toolbar world').pack(padx=30,pady=30)
        self.makeToolbar()

    def makeToolbar(self):
        toolbar = Frame(self,cursor='hand2',relief=SUNKEN,bd=2)
        toolbar.pack(side=TOP,fill=X)
        Button(toolbar,text='Quit',command=self.quit).pack(side=RIGHT)
        Button(toolbar,text='Hello',command=self.greeting).pack(side=LEFT)

    def makeMenuBar(self):
        self.menubar = Frame(self,relief=RAISED ,bd=2)
        self.menubar.pack(side=TOP,fill=X)
        self.fileMenu()
        self.editMenu()

    def fileMenu(self):
        mbutton = Menubutton(self.menubar,text = 'File',underline=0)
        mbutton.pack(side=LEFT)
        menu = Menu(mbutton)
        menu.add_command(label='New',command=self.notdone)
        menu.add_command(label='Open',command=self.notdone)
        menu.add_command(label='Quit',command=self.quit)
        mbutton['menu'] = menu
        return mbutton


    def editMenu(self):
        mbutton = Menubutton(self.menubar,text='Edit',underline=0)
        mbutton.pack(side=LEFT)
        menu = Menu(mbutton)
        menu.add_command(label='Cut',command=self.notdone)
        menu.add_command(label='Paste',command=self.notdone)
        menu.add_separator()

        submenu = Menu(menu)
        submenu.add_command(label='Spam',command=self.notdone)
        submenu.add_command(label='Eggs',command=self.greeting)
        menu.add_cascade(label='Stuff',menu=submenu)

        menu.add_command(label='Delete',command=self.greeting)
        #menu.entryconfig(2,state=DISABLED)
        mbutton['menu'] = menu
        return mbutton

    def greeting(self):
        Dialog(self,title = 'greeting',
        text = 'Howdy',
        bitmap = '', default=0,strings=('hi',))

    def notdone(self):
        Dialog(self,title = 'Not implemented',
        text = 'Not yet available',
        bitmap = 'error',default = 0,strings=('OK',) )

    def quit(self):
        ans = Dialog(self, title = 'Verify quit ',
        text = 'Are you sure you want to quit?',
        bitmap = 'question',
        default = 1,
        strings = ('Yes','No'))

if __name__ == '__main__': Hello().mainloop()
