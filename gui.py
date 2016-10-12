#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter

class lyrics_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        
    def initialize(self):
        self.grid()
        button = Tkinter.Button(self,text=u"Click me !")
        button.grid(column=0,row=0)


if __name__ == "__main__":
    app = lyrics_tk(None)
    app.title('iTunes Lyrics')
    app.mainloop()
