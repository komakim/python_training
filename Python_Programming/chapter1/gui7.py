from Tkinter import *
from Dialog import Dialog

class Hello(Frame):
    def __init__ (self,master=None):
        Frame.__init__(self,master)
        Pack.config(self)
        self.createWidgets()

    def greet(self):
        print "hi"

    def createWidgets(self):
        Label(self,text='Hello popuo world!').pack(side=TOP)
        Button(self,text='Pop1',command=self.dialog1).pack()
        Button(self,text='Pop2',command=self.dialog2).pack()
        Button(self,text='hey',command=self.greet).pack(side=LEFT)
        Button(self,text='bye',command=self.quit).pack(side=RIGHT)
    def dialog1(self):
        ans = Dialog(self,
        title = 'popup fun!',
        text = 'an example',
        bitmap = 'questhead',
        default = 0,
        strings = ('yes','no','cancel')
        )
        if ans.sum == 0:
            self.dialog2()

    def dialog2(self):
        Dialog(self,
        title = 'HAL-9000',
        text = "I'm afraid I can't let you do that, Dave",
        bitmap = 'hourglass',
        default = 0,
        strings = ('spam','SPAM')
        )

if __name__ == '__main__':Hello().mainloop()
