import os
from tkinter import *

monitor = Tk()
monitor.configure(background='black')
monitor.attributes("-fullscreen",True)
width = monitor.winfo_screenwidth()
height = monitor.winfo_screenheight()
clock_label = Label(monitor,text=" ", fg="White", font=myFont, bg="Black")
clock_label.place(x=width*0.35,y=height*0.05)
loading_label = Label(monitor,text="Updating...", fg="White", font=myFont, bg="Black")
loading_label.place(x=width*0.25,y=height*0.35)
os.system("cd ~/WienerLinienPythonAbfahrtsmonitor/ && git pull")
loading_label.configure(text="Loading...")
os.system("cd ~/WienerLinienPythonAbfahrtsmonitor/ && python3 .")
monitor.mainloop()

