#HW6 - Spectrogram
#Author - Rajesh Narayan

import wave
import struct
import numpy as np
import math
import image

"""Opens the audio file, unpacks each of the datapoints, and appends them to a list."""
raw = wave.open("sx222.wav", "rb")

sample_list = []
for i in range(raw.getnframes()):

	frame = raw.readframes(1)
	sample_value = struct.unpack('h', frame)
	sample_list.append(sample_value[0])

    
"""Creates windows at intervals of 10 ms, with each window having a length of 25 ms."""
listofwindows = []
n = 0
for n in range(0, (raw.getnframes()-401), 160):
	window_size = n+400
	window = []
	for k in range(n,window_size):
		window.append(sample_list[k])
	listofwindows.append(window)

    
"""Computes the Fast Fourier Transform for all the windows, and appends them to a new list."""    
listoflists = []
for i in range(len(listofwindows)):
	listoflists.append(np.fft.fft(listofwindows[i]))

    
"""Takes the list of lists of values which have gone through the FFT, and converts them to log magnitudes. Furthermore, it then converts them to log scale with the formula 10*log10 square magnitude."""
listofmagnitudes = []
for i in range(len(listoflists)):
    listofmags1 = []
    for j in range(len(listoflists[i])):
        real = (listoflists[i][j]).real
        imaginary = (listoflists[i][j]).imag
        listofmags1.append(10 * math.log(math.sqrt((real**2)+(imaginary**2))))
    listofmagnitudes.append(listofmags1)
amin = np.amin(listofmagnitudes)
amax = np.amax(listofmagnitudes)


"""Takes the final 2D list, along with the minimum and maximum values in the list, and turns them into an image with set pixel colors."""
win = image.ImageWin("Spectrogram",len(listofmagnitudes),len(listofmagnitudes[0]))
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