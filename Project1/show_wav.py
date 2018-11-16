#!/usr/bin/python
from scipy.io import wavfile
from matplotlib import pyplot as plt
import numpy as np

# load the wav file and calculate the time 
sample_rate, data = wavfile.read('DSP.wav')
times = np.arange(len(data))/float(sample_rate)
#print(data.shape)
#print(len(data))
#print(data.size)

# .ndim: Number of array dimensions
# get the channels number
if data.ndim > 1:
    sample_num, channel_num = data.shape
    data = data.sum(axis = 1)
else:
    channel_num = 1
    sample_num = data.shape[0]

# show the waveform
plt.plot(times, data/32768)
plt.title('Speech Signal', fontsize = 18)
plt.xlabel('time')
plt.ylabel('amplitude')
#plt.show()
plt.savefig('show_signal.png')
