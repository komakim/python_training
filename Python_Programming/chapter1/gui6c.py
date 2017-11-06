from Tkinter import *
from gui6 import Hello

class HelloSubclass(Hello):
    def quit(self):
        print 'Hello'

    def make_widgets(self):
        Hello.make_widgets(self)

        Button(self,
        text = 'Extend',
        command = lambda x=self:
        Hello.quit(x)).pack(side=RIGHT)

if __name__ == '__main__': HelloSubclass().mainloop()
