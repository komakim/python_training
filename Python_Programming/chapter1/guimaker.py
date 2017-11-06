from Tkinter import *
from types import *

class GuiMaker(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack(expand=YES,fill=BOTH)
        self.start()
        self.makeMenuBar()
        self.makeWidgets()
        self.makeToolBar()

    manuBar = []
    toolBar = []
    helpButton = 1

    def makeMenuBar(self):
        menubar = Frame(self,relief=RAISED,bd=2)
        menubar.pack(side = TOP,expand=YES,fill=X)

        for entry in self.menuBar:
            mbutton = Menubutton(menubar,text=entry[0],
            underline=entry[1])
            mbutton.pack(side=LEFT)
            menu = self.addMenuItems(mbutton,entry[2])
            mbutton['menu'] = menu
        if self.helpButton:
            Button(menubar,text='Help',
            cursor='gumby',
            relief = FLAT,
            command = self.help).pack(side=RIGHT)

    def addMenuItems(self,parent,items):
        menu = Menu(parent)
        for item in items:
            if item == 'separator':
                menu.add_separator({})
            elif type(item[2]) != ListType:
                menu.add_command(
                label= item[0],
                underline = item[1],
                command = item[2]
                                )
            else:
                submenu = self.addMenuItems(menu,item[2])
                menu.add_cascade(
                label = item[0],
                underline = item[1],
                menu = submenu
                )
        return menu

    def makeToolBar(self):
        toolbar = Frame(self,cursor = 'hand2',relief=SUNKEN,bd=2)
        for item in self.toolBar:
            Button(toolbar,text=item[0],command=item[1]).pack(item[2])

    def makeWidgets(self):
        name = Label(self,
        text = self.__class__.__name__ ,
        cursor = 'crosshair')
        name.pack(padx = 50, pady = 50 ,expand=YES,fill=BOTH)

if __name__ == '__main__':
    from guimixin import *
    class TestApp(GuiMixin,GuiMaker):
        #helpButton = 0
        def start(self):
            self.menuBar = [(
            'File',0,
            [('Quit',0,self.quit)]
            )]
            self.toolBar = [
            ('Quit',self.quit,{'side':LEFT})
            ]

    TestApp().mainloop()
