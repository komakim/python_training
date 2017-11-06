PDIR = '/usr/bin/python'

from Tkinter import *
from Dialog import Dialog
from ScrolledText import ScrolledText

class GuiMixin:
    def question(self,title,text,bitmap='question',strings=('Yes','No')):
        return Dialog(self,
        title = title,
        text = text,
        bitmap = bitmap,
        default = 1,
        strings=strings).num

    def infobox(self,title,text,bitmap='',strings=('OK',)):
        Dialog(self,
        title=title,text=text,bitmap=bitmap,default=0,strings=strings)

    def quit(self):
        ans = self.question('Varify quit','Are you sure you want to quit?')
        if ans == 0 :
            Frame.quit(self)

    def notdone(self):
        self.infobox('Not implemented','Option not available','error')

    def help(self):
        self.infobox('RTFM','See figure 1 ... ','info')

    def errorbox(self,text):
        self.infobox('ERROR!',text,'error')

    def clone(self):
        new = Toplevel()
        myclass = self.__class__
        myclass(new)

    def spawn(self,demo,fork=0):
        import os
        try:
            obase = os.environ['PYTHONBASE']
        except:
            pbase = PDIR
        python = pbase + '/python'
        if not fork:
            os.system('%s %s /Demo/tkinter/%s' % (python, pbase, demo))
        else:
            pid = os.fork()
            if pid == 0:
                os.execv(python,(python,[base+'/Demo/tkinter/'+demo]))

    def browser(self,file):
        new = Toplevel()
        text = ScrolledText(new,height=30,width=90);text.Pack()

        new.title("Poor-man's Text Editor")
        new.iconname("browser")
        text.insert('0.0',open(file,'r').read())

if __name__ == '__main__':
    class TestMixin(GuiMixin,Frame):
        def __init__(self,parent=None):
            Frame.__init__(self,parent)
            self.pack()
            Button(self,text='quit',command=self.quit).pack(fill=X)
            Button(self,text='help',command=self.help).pack(fill=X)
            Button(self,text='clone',command=self.clone).pack(fill=X)
    TestMixin().mainloop()
