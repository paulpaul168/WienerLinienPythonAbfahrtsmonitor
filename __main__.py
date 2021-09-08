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
	dwagen_T.configure(text=str(D_1)+ "min")
	dwagen2_T.configure(text=str(D_2)+ "min")
#	b400 = Label(monitor,text="400 ", fg="White", font=myFont, bg="Black")
#	b400.place(x=width*0.1,y=height*0.65)
	monitor.after(TIME_RESTART, updateData)


def updateData():
	try:
		nussdorf = getResponse('https://www.wienerlinien.at/ogd_realtime/monitor?rbl=90')
		j_obj_nussdorf = json.loads(nussdorf.decode())
		if len(j_obj_nussdorf['data']['monitors'][0]['lines'][0]['departures']['departure']) == 2:
			D_1 = j_obj_nussdorf['data']['monitors'][0]['lines'][0]['departures']['departure'][0]['departureTime']['countdown']
			D_2 = j_obj_nussdorf['data']['monitors'][0]['lines'][0]['departures']['departure'][1]['departureTime']['countdown']
		else:
			D_1 = j_obj_nussdorf['data']['monitors'][0]['lines'][0]['departures']['departure'][0]['departureTime']['countdown']
			D_2 = D_1
		print("D1: "+str(D_1)+"min ; D2: "+str(D_2)+"min")
		drawData(D_1,D_2)
		loading_label.configure(text=" ")
		dwagen.configure(text="D ")
	except:
		dwagen.configure(text="Error!")

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
	loading_label = Label(monitor,text="Updating...", fg="White", font=myFont, bg="Black")
	loading_label.place(x=width*0.25,y=height*0.35)
	time.sleep(0.5)
	os.system("cd ~/WienerLinienPythonAbfahrtsmonitor/ && git pull")
	loading_label.configure(text="Loading...")
	dwagen = Label(monitor,text="D ", fg="White", font=myFont, bg="Black")
	dwagen.place(x=width*0.07,y=height*0.25)
	dwagen_T = Label(monitor,text="? min", fg="White", font=myFont, bg="Black")
	dwagen_T.place(x=width*0.7,y=height*0.25)
	dwagen2 = Label(monitor,text="D ", fg="White", font=myFont, bg="Black")
	dwagen2.place(x=width*0.07,y=height*0.55)
	dwagen2_T = Label(monitor,text="? min", fg="White", font=myFont, bg="Black")
	dwagen2_T.place(x=width*0.7,y=height*0.55)

	monitor.after(TIME_RESTART, updateData)
	monitor.after(1000, updateClock)
	monitor.mainloop()
