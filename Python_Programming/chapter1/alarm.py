#1! /usr/local/bin/python
from Tkinter import *

class Alarm(Frame):
    def repeater(self):
        self.bell()
        self.after(self.msecs,self.repeater)
    def __init__(self,msecs=1000):
        Frame.__init__(self)
        self.msecs = msecs
        self.pack()
        self.repeater()
        Button(self,text='Stop the beeps!',command = self.quit).pack()
if __name__ == '__main__': Alarm(50).mainloop()
