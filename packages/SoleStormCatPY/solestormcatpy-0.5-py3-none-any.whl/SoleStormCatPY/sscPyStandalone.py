"""This is the standalone app for 'SoleStormCatPY'. Here, any user can use 'SoleStormCatPY' with little to no coding (Depends on if the user uses a script to open this script). Here is how you can make your own script to open this app:

import SoleStormCatPY.sscPyStandalone as SSCstand

SSCstand.fullPythonApp()
"""

from tkinter import *
from tkinter.ttk import *
from time import strftime

"Apps"
def WebGUI():
	import SoleStormCatPY.WebOpen
	SoleStormCatPY.WebOpen.webGUI()
def TerminalGUI():
	import SoleStormCatPY.terminal
	SoleStormCatPY.terminal.terminalGUI()
def SystemInfo():
	import SoleStormCatPY.SystemInfo as si
	si.systemInfoPrint(deviceOS,userName,pythonVersion)
def ClockTimerGUI():
	import SoleStormCatPY.ClockTimerGUI
	
"App Loader:"
def fullPythonApp():
	frame = Tk()
	frame.title('SoleStormCatPY')
	frame.geometry('1024x768')
	
	MenuBar = Menu(frame)
	file = Menu(MenuBar, tearoff=0)
	MenuBar.add_cascade(label ="File", menu = file)
	file.add_command(label ="Quit", command=quit)
	
	appsBar = Menu(MenuBar, tearoff=0)
	MenuBar.add_cascade(label ="Apps", menu = appsBar)
	appsBar.add_command(label ="ClockTimer", command=ClockTimerGUI)
	appsBar.add_command(label ="System Info", command=SystemInfo)
	appsBar.add_command(label ="Terminal", command=TerminalGUI)
	appsBar.add_command(label ="Web", command=WebGUI)
	
	appLabel = Label(frame, text = 'Welcome to "SoleStormCatPY"! Please choose an app below!')
	appLabel.pack()
	
		
	WebB = Button(frame,text='Web', command=lambda: WebGUI())
	WebB.pack()
	
	
	TerminalB = Button(frame,text='Terminal', command=lambda: TerminalGUI())
	TerminalB.pack()
	
	
	SystemInfoB = Button(frame,text='System Info', command=lambda: SystemInfo())
	SystemInfoB.pack()
	
		
	ClockTimerB = Button(frame,text='ClockTimer', command=lambda: ClockTimerGUI())
	ClockTimerB.pack()
	
	frame.config(menu = MenuBar)
	frame.mainloop()
