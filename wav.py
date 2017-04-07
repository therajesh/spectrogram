import wave
import struct
import numpy as np
#from numpy import array
#from pylab import *
#import matplotlib.pyplot as plt 

raw = wave.open("sx222.wav", "rb")
n = 0
frame_number = raw.getnframes()
frame_width = raw.getsampwidth()
frame_rate = raw.getframerate()
frame_channels = raw.getnchannels()
#wave_frames = raw.readframes(-1)
#plt.title("Try")
#plt.plot(wave_frames)
#plt.show()
#print(raw)

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
#print(len(listofwindows))
#print(len(listofwindows[0]))

listoflists = []
for i in range(len(listofwindows)):
	listoflists[i] = np.fft.fft(listofwindows[i])
print (len(listoflists))
	