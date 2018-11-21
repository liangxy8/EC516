#!/usr/bin/python
from matplotlib import pyplot as plt
from scipy import fftpack
from scipy.io import wavfile
import numpy as np


[sample_rate, data] = wavfile.read('DSP.wav')

#a = np.sum(data)
#print(data)
#print(a)
if data.ndim > 1:
    sample_num, channel_num = data.shape
    data = data.sum(axis = 1)
else:
    channel_num = 1
    sample_num = data.shape[0]
length_window = int(0.02*sample_rate)
#print(data.shape)
print("the length of window is:",length_window)
L = int(input("please input L:",))
if L > length_window:
    print("Speech signal will lost")


data = np.append(data, np.zeros(length_window))
#print(len(data))
#print(sample_num)
#for n in range(0, len(data)-length_window+L, L):
#    spectrum_in_window = fftpack.fft(data[n:n+length_window])
#    spectrum = np.vstack((spectrum, spectrum_in_window))
#print(spectrum_in_window)

spectrum = fftpack.fft(data[0:length_window])
for n in range(length_window+1, sample_num, L):
    spectrum_in_window = fftpack.fft(data[n:n+length_window])
    spectrum = np.vstack((spectrum, spectrum_in_window))




