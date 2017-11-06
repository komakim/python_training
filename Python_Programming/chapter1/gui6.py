from Tkinter import *
class Hello(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.pack()
        self.make_widgets()
    def make_widgets(self):
        widget = Button(self,text='Hello framework world!',
        command =self.quit)
        widget.pack(side=LEFT)

if __name__ =='__main__':
    Hello().mainloop()
