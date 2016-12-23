#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Foundation import *
from ScriptingBridge import *

import time

import Tkinter
from PyLyrics import *

iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")

t_end = time.time() + 10

lines = 0
def parse_text(text):
    first = u''
    second = u''
    third = u''
    count = 0
    for character in text:
        if character == "\n":
            count +=1
        if count>50 and count <=100:
            second = second + character
        elif count>100:
            third = third + character
        else:
            first = first + character
    return [first,second,third]

class lyrics_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.ff = u''
        self.ss = u''
        self.tt = u''
        self.initialize()
    
    def set_text(self):
        self.labelVariable.set(self.ff)
        self.labelVariable2.set(self.ss)
        self.labelVariable3.set(self.tt)

    def initialize(self):
        self.grid()
        button = Tkinter.Button(self,text=u"Get Lyrics",command=self.OnButtonClick)
        button.grid(column=0,row=0)

        self.labelVariable = Tkinter.StringVar()
        self.labelVariable2 = Tkinter.StringVar()
        self.labelVariable3 = Tkinter.StringVar()

        label = Tkinter.Label(self,textvariable=self.labelVariable, anchor="w",fg="white",bg="black")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        
        label2 = Tkinter.Label(self,textvariable=self.labelVariable2, anchor="w",fg="white",bg="black")
        label2.grid(column=2,row=1,columnspan=2,sticky='EW')
        
        label3 = Tkinter.Label(self,textvariable=self.labelVariable3, anchor="w",fg="white",bg="black")
        label3.grid(column=4,row=1,columnspan=2,sticky='EW')

    def OnButtonClick(self):
        track = iTunes.currentTrack()
        name = str(track.name())
        artist = str(track.artist())
        try:
            lyrics = PyLyrics.getLyrics(artist,name)
        except:
            first = unicode("Sorry man.","utf-8")
        lines = parse_text(lyrics)
        self.ff = lines[0]
        self.ss = lines[1]
        self.tt = lines[2]
        self.set_text()

if __name__ == "__main__":
    app = lyrics_tk(None)
    app.title('iTunes Lyrics')
    app.mainloop()
