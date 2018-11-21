#!/usr/bin/python
from matplotlib import pyplot as plt
from scipy import fftpack
from scipy.io import wavfile
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

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

spectrum = fftpack.fft(data[0:length_window])
for n in range(L, sample_num, L):
    print(n)
    spectrum_in_window = fftpack.fft(data[n:n+length_window])
    spectrum = np.vstack((spectrum, spectrum_in_window))

fig = plt.figure()
ax = Axes3D(fig)
xs = np.arange(spectrum.shape[0])
ys = np.arange(spectrum.shape[1])
xs,ys = np.meshgrid(xs,ys)
sign = np.sign(spectrum.real)
amplitude = abs(spectrum)*sign
zs = np.log10(np.transpose(amplitude))
surf = ax.plot_surface(xs,ys,zs,cmap = cm.coolwarm, linewidth = 0, antialiased = False)
ax.set_xlabel('n')
ax.set_ylabel('omega')
ax.set_zlabel('power of 10')
plt.savefig('discrete_DTFT.png')
