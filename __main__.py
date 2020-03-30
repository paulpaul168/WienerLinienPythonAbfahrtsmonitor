from tkinter import *
import json, urllib.request, time, os

TIME_RESTART = 20000 #in ms
myFont = ("Times New Roman", 72)

def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
       data = operUrl.read()
    else:
       print("Error receiving data", operUrl.getcode())
    return data

def drawData(D_1, D_2):
	dwagen = Label(monitor,text="D ", fg="White", font=myFont, bg="Black")
	dwagen.place(x=width*0.07,y=height*0.25)
	dwagen_T = Label(monitor,text=str(D_1)+" min", fg="White", font=myFont, bg="Black")
	dwagen_T.place(x=width*0.7,y=height*0.25)
	dwagen2 = Label(monitor,text="D ", fg="White", font=myFont, bg="Black")
	dwagen2.place(x=width*0.07,y=height*0.55)
	dwagen2_T = Label(monitor,text=str(D_2)+" min", fg="White", font=myFont, bg="Black")
	dwagen2_T.place(x=width*0.7,y=height*0.55)

#	b400 = Label(monitor,text="400 ", fg="White", font=myFont, bg="Black")
#	b400.place(x=width*0.1,y=height*0.65)
	monitor.after(TIME_RESTART, updateData)


def updateData():
	try:
		nussdorf = getResponse('https://www.wienerlinien.at/ogd_realtime/monitor?rbl=90')
		j_obj_nussdorf = json.loads(nussdorf.decode())
		D_1 = j_obj_nussdorf['data']['monitors'][0]['lines'][0]['departures']['departure'][0]['departureTime']['countdown']
		D_2 = j_obj_nussdorf['data']['monitors'][0]['lines'][0]['departures']['departure'][1]['departureTime']['countdown']
		print("D1: "+str(D_1)+"min ; D2: "+str(D_2)+"min")
		drawData(D_1,D_2)
		loading_label.configure(text=" ")
	except:
		dwagen = Label(monitor,text="Error! ", fg="White", font=myFont, bg="Black")
		dwagen.place(x=width*0.1,y=height*0.25)
def updateClock():
	now = time.strftime("%H:%M:%S")
	clock_label.configure(text=now)
	monitor.after(1000, updateClock)

if __name__ == "__main__":
	monitor = Tk()
	monitor.configure(background='black')
	monitor.attributes("-fullscreen",True)
	width = monitor.winfo_screenwidth()
	height = monitor.winfo_screenheight()
	clock_label = Label(monitor,text=" ", fg="White", font=myFont, bg="Black")
	clock_label.place(x=width*0.35,y=height*0.05)
	loading_label = Label(monitor,text="Loading...", fg="White", font=myFont, bg="Black")
	loading_label.place(x=width*0.25,y=height*0.35)
	#os.system("cd ~/WienerLinienPythonAbfahrtsmonitor/ && git pull")
	#loading_label.configure(text="Loading...")
	monitor.after(TIME_RESTART, updateData)
	monitor.after(1000, updateClock)
	monitor.mainloop()
