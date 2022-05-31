import os

import pyautogui
import keyboard
import gtts
import playsound
import threading
import time
import tkinter
from tkinter import ttk
pyautogui.PAUSE = 0
errortts = gtts.gTTS("Sorry! This key is an invalid macro key.")
errortts.save("error.mp3")
enabledtts = gtts.gTTS("Starting macro.")
enabledtts.save("start.mp3")
disabledtts = gtts.gTTS("Stopping macro.")
disabledtts.save("stop.mp3")
path = os.getcwd().replace('\\', '/')
enabled = False
macroKey = ''
enableKey = '/'
def toggleMacro():
    global enabled
    global cpsInput
    time.sleep(1)
    try:
        '''if enabled:
            playsound.playsound(f'{path}/stop.mp3')
        else:
            playsound.playsound(f'{path}/start.mp3')'''
        enabled = not enabled
    except:
        pass
def macro():
    global enabled
    while True:
        #enableKey = enableInput.get() NOT WORKING YET
        if enableKey != '':
            if keyboard.is_pressed(enableKey):
                toggleMacro()
        if enabled:
            macroKey = macroInput.get()
            inputSpeed = 1 / float(ipsInput.get())
            if float(ipsInput.get()) >= 65:
                inputSpeed=0
            if macroKey == 'left click':
                pyautogui.leftClick(interval=inputSpeed)
            elif macroKey == 'right click':
                pyautogui.rightClick(interval=inputSpeed)
            elif macroKey == 'middle click':
                pyautogui.middleClick(interval=inputSpeed)
            else:
                if macroKey not in pyautogui.KEYBOARD_KEYS:
                    enabled = False
                    playsound.playsound(f'{path}/error.mp3')
                pyautogui.press(macroKey, interval=inputSpeed)
root = tkinter.Tk()
root.title("UltiMacro v0.5.1")
frame = ttk.Frame(root, padding=8)
frame.grid()
ttk.Label(frame, text="UltiMacro").grid(row=0, column=0)
ttk.Button(frame, text="Quit", command=root.destroy).grid(row=10, column=10)
macroInput = ttk.Entry(frame, text="Macro")
macroInput.grid(row=3, column=2)
ipsInput = ttk.Entry(frame, text="IPS")
ipsInput.grid(row=3, column=5)
'''enableInput = ttk.Entry(frame, text="Toggle")
enableInput.insert(tkinter.END, '/')
enableInput.grid(row=3, column=8)
NOT WORKING YET'''
ttk.Label(frame, text="Macro").grid(row=2, column=2)
ttk.Label(frame, text="Inputs Per Second").grid(row=2, column=5)
#ttk.Label(frame, text="Toggle Key").grid(row=2, column=8) NOT WORKING YET
macroThread = threading.Thread(target=macro)
macroThread.start()
print("UltiMacro Running")
root.mainloop()
