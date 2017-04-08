import wave
import struct
import numpy as np
import math
import image

raw = wave.open("sx222.wav", "rb")
n = 0
frame_number = raw.getnframes()
frame_width = raw.getsampwidth()
frame_rate = raw.getframerate()
frame_channels = raw.getnchannels()


sample_list = []
for i in range(raw.getnframes()):

	frame = raw.readframes(1)
	sample_value = struct.unpack('h', frame)
	sample_list.append(sample_value[0])

#for j in range (1, 43001):
#	if (j%1000 == 0):
#		print (sample_list[j])
#print (frame_rate)

listofwindows = []
n = 0
for n in range(0, (raw.getnframes()-401), 160):
	window_size = n+400
	window = []
	for k in range(n,window_size):
		window.append(sample_list[k])
	listofwindows.append(window)

    

listoflists = []
for i in range(len(listofwindows)):
	listoflists.append(np.fft.fft(listofwindows[i]))


listofmagnitudes = []
for i in range(len(listoflists)):
    listofmags1 = []
    for j in range(len(listoflists[i])):
        m = (listoflists[i][j]).real
        n = (listoflists[i][j]).imag
        listofmags1.append(10 * math.log(math.sqrt((m**2)+(n**2))))
    listofmagnitudes.append(listofmags1)
amin = np.amin(listofmagnitudes)
amax = np.amax(listofmagnitudes)

'''for i in range(len(listofmagnitudes)):
    listofmagnitudes[i] = (listofmagnitudes[i])**(1/2)
    for j in range(len(listofmagnitudes[i])):
        listofmagnitudes[i][j] = 10* math.log10(listofmagnitudes[i][j])
#print (listofmagnitudes[i])'''


win = image.ImageWin("My Window",len(listofmagnitudes),len(listofmagnitudes[0]))
myImage = image.EmptyImage(len(listofmagnitudes),len(listofmagnitudes[0]))
for row in range(myImage.getHeight()):
    for col in range(myImage.getWidth()):
        i = (255*((listofmagnitudes[col][row] - amin)/(amax-amin)))
        v = myImage.getPixel(col,row)
        v.red = 255 - i
        v.green = 255 - i
        v.blue = 255 - i
#            x = map(lambda x: 255-x, v)
        myImage.setPixel(col,row,v)
myImage.setPosition(0,0)
myImage.draw(win)
win.exitOnClick()