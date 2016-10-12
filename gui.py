#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Foundation import *
from ScriptingBridge import *

import time

import Tkinter
from PyLyrics import *

iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")


class lyrics_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        
    def initialize(self):
        self.grid()
        button = Tkinter.Button(self,text=u"Get Lyrics",command=self.OnButtonClick)
        button.grid(column=0,row=0)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable, anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')

    def OnButtonClick(self):
        track = iTunes.currentTrack()
        name = str(track.name())
        artist = str(track.artist())
        lyrics = PyLyrics.getLyrics(artist,name)
        self.labelVariable.set(lyrics)

if __name__ == "__main__":
    app = lyrics_tk(None)
    app.title('iTunes Lyrics')
    app.mainloop()
