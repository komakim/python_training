from Tkinter import *
def quit():
    print 'Hello, I must be going ...'
    import sys; sys.exit()

widget = Button(None,text='Hello widget world',command = quit)
widget.pack()
widget.mainloop()
