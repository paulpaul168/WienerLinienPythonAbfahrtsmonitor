import tkinter, json, urllib.request

TIME_RESTART = 20000 #in ms

def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
       data = operUrl.read()
    else:
       print("Error receiving data", operUrl.getcode())
    return data


def updateData():
	nussdorf = getResponse('https://www.wienerlinien.at/ogd_realtime/monitor?rbl=90')
	j_obj_nussdorf = json.loads(nussdorf.decode())
	D_1 = j_obj_nussdorf['data']['monitors'][0]['lines'][0]['departures']['departure'][0]['departureTime']['countdown']
	D_2 = j_obj_nussdorf['data']['monitors'][0]['lines'][0]['departures']['departure'][1]['departureTime']['countdown']
	print("D1: "+str(D_1)+"min ; D2: "+str(D_2)+"min")
	monitor.after(TIME_RESTART, updateData)


if __name__ == "__main__":
	monitor = tkinter.Tk()
	monitor.configure(background='black')
	monitor.attributes("-fullscreen",True)
	width = monitor.winfo_screenwidth()
	height = monitor.winfo_screenheight()
	monitor.after(TIME_RESTART, updateData)
	monitor.mainloop()
