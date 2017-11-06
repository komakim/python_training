#/usr/local/bin/python

from Tkinter import *
from guimixin import GuiMixin
from guimaker import GuiMaker

class Hello(GuiMixin,GuiMaker):
    def start(self):
        self.hellos = 1
        self.master.title("GuiMaker Demo")
        self.master.iconname("GuiMaker")

        self.menuBar = [
        ('File',0,
        [('New...',0,self.notdone),
        ('Open',0,self.fileOpen),
        ('Quit',0,self.quit)
        ]
        ),
        ('Edit',0,
        [('Cut',-1,lambda:0),
        ('Paste',-1,lambda:0),
        'separator',
        ('Stuff',-1,
            [('Clone',-1,self.clone),
            ('More',-1,self.more)]
        ),
        ('Detele',-1,lambda:0),
        [5]
        ]),

        ('Play',0,
        [('Hello',0,self.greeting),
        ('Popup',0,self.dialog),
        ('Demos',0,
        [('Hanoi',-1,lambda x=self:x.spawm('guido/hanoi.py',1)),
        ('Pong',-1,lambda x=self: x.spawn('matt/pong-demo-1.py'))]
        )]
        )]

        self.toolBar=[
        ('Quit',self.quit,{'side':RIGHT}),
        ('Hello',self.greeting,{'side':LEFT}),
        ('Popup',self.dialog,{'side':LEFT,'expand':YES})
        ]

    def makeWidgets(self):
        middle = Label(self,text='Hello maker world',cursor='pencil')
        middle.pack(padx=50,pady=50,expand=YES,fill=BOTH)

    def greeting(self):
        self.hellos =self.hellos + 1
        if self.hellos % 3 :
            print "hi"
        else:
            self.infobox("Gocya",'HELLO!')
    def dialog(self):
        button = self.question('OOPS!',
        'You typed "rm*" continue?',
        'questhead',('yes','no','help'))
        [lambda:0,self.quit,self.help][button]()

    def fileOpen(self):
        self.browser('big_gui2.py')

    def more(self):
        new = Toplevel()
        Label(new,text='A new non-modal window').pack()
        Button(new,text='Quit',command=self.quit).pack(side = LEFT)
        Button(new,text='More',command=self.more).pack(side = RIGHT)

if __name__ == '__main__':
    Hello().mainloop()
