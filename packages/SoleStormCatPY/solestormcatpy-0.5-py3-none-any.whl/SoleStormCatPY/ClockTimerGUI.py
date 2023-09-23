"""THIS IS THE GUI COUNTERPART OF 'ClockTimer'! HERE IS HOW TO USE:
import SoleStormCatPY.ClockTimerGUI
"""
import tkinter
import tkinter.ttk as ttk
from threading import Timer
from playsound import playsound

def timeout():
    frameEND = tkinter.Tk()
    frameEND.title('Timer, ENDED!')
    frameEND.geometry('500x500')
    
    lblEND = tkinter.Label(frameEND,
    text = "Your Timer Has Ended!")
    lblEND.pack()
    
    playsound('ClockTimerAssets//timerUP.wav')
    frameEND.mainloop()
    
def clockTimerGUI():
    timeSTR = inputtxt.get(1.0, 'end-1c')
    time = int(timeSTR)
    
    t = Timer(time, timeout)
    t.start()
    
    frameTime = tkinter.Tk()
    frameTime.title('Timer, Started')
    frameTime.geometry('500x500')
    
    lblTime = tkinter.Label(frameTime,
    text = "Your Timer Of:")
    lblTime.pack()
    
    lbltimeS = tkinter.Label(frameTime,
    text = timeSTR)
    lbltimeS.pack()
    
    lbltime1 = tkinter.Label(frameTime,
    text = "Seconds has started!")
    lbltime1.pack()
    
    frameTime.mainloop()
    
    t.join()
def clockTimerGUImin():
    timeSTR = inputtxt.get(1.0, "end-1c")
    time = int(timeSTR)
        
    t = Timer(time * 60, timeout)
    t.start()
    
    frameTime = tkinter.Tk()
    frameTime.title('Timer, Started')
    frameTime.geometry('500x500')
    
    lblTime = tkinter.Label(frameTime,
    text = "Your Timer Of:")
    lblTime.pack()
    
    lbltimeS = tkinter.Label(frameTime,
    text = timeSTR)
    lbltimeS.pack()
    
    lbltime1 = tkinter.Label(frameTime,
    text = "Minutes Has Started!")
    lbltime1.pack()
    
    frameTime.mainloop()
    
    t.join()
    
def clockTimerGUIhour():
    timeSTR = inputtxt.get(1.0, "end-1c")
    time = int(timeSTR)
    
    t = Timer(time * 3600, timeout)
    t.start()
    
    frameTime = tkinter.Tk()
    frameTime.title('Timer, Started')
    frameTime.geometry('500x500')
    
    lblTime = tkinter.Label(frameTime,
    text = "Your Timer Of:")
    lblTime.pack()
    
    lbltimeS = tkinter.Label(frameTime,
    text = timeSTR)
    lbltimeS.pack()
    
    lbltime1 = tkinter.Label(frameTime,
    text = "Hours Has Started!")
    lbltime1.pack()
    
    lbltimeD = tkinter.Label(frameTime,
    text = "DISCLAIMER: THIS WILL TAKE A WHILE!")
    lbltimeD.pack()
    
    frameTime.mainloop()
    t.join()

frame = tkinter.Tk()
frame.title('Timer')
frame.geometry('1000x250')
tabControl = ttk.Notebook(frame)

tabSEC = ttk.Frame(tabControl)
tabMIN = ttk.Frame(tabControl)
tabHOUR = ttk.Frame(tabControl)
tabControl.add(tabSEC, text='Seconds')
tabControl.add(tabMIN, text='Minutes')
tabControl.add(tabHOUR, text='Hours')
tabControl.pack(expand = 1, fill ="both")


lblBLANK = tkinter.Label(tabSEC,
text = " ")
lblBLANK.pack()
lblBLANK = tkinter.Label(tabMIN,
text = " ")
lblBLANK.pack()
lblBLANK = tkinter.Label(tabHOUR,
text = " ")
lblBLANK.pack()

inputtxt = tkinter.Text(tabSEC,
height = 1,
width = 45)
inputtxt.pack()
inputtxt = tkinter.Text(tabMIN,
height = 1,
width = 45)
inputtxt.pack()
inputtxt = tkinter.Text(tabHOUR,
height = 1,
width = 45)
inputtxt.pack()

startTimerButton = tkinter.Button(tabSEC,
text = "Start Timer",
command = clockTimerGUI)
startTimerButton.pack()
startTimerButton = tkinter.Button(tabMIN,
text = "Start Timer",
command = clockTimerGUImin)
startTimerButton.pack()
startTimerButton = tkinter.Button(tabHOUR,
text = "Start Timer",
command = clockTimerGUIhour)
startTimerButton.pack()


lbl = tkinter.Label(tabSEC,
text = "Enter your time in the box, then click the 'Start Timer' button. You may use the tabs to change your time setting, your current time setting is: Seconds")
lbl.pack()
lbl = tkinter.Label(tabMIN,
text = "Enter your time in the box, then click the 'Start Timer' button. You may use the tabs to change your time setting, your current time setting is: Minutes")
lbl.pack()
lbl = tkinter.Label(tabHOUR,
text = "Enter your time in the box, then click the 'Start Timer' button. You may use the tabs to change your time setting, your current time setting is: Hours")
lbl.pack()

frame.mainloop()
