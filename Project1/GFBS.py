import numpy as np
from matplotlib import pyplot as plt
from scipy import fftpack
from scipy.io import wavfile
#import dTDFT


#sample_rate, data = dTDFT.sample_rate, dTDFT.data
#sample_num = dTDFT.sample_num
#length_window = dTDFT.length_window
#L = dTDFT.L
#spectrum = dTDFT.spectrum
#print(spectrum.shape)


[sample_rate, data] = wavfile.read('DSP.wav')
if data.ndim > 1:
    sample_num, channel_num = data.shape
    data = data.sum(axis = 1)
else:
    channel_num = 1
    sample_num = data.shape[0]
length_window = int(0.02*sample_rate)
print("the length of window is:",length_window)
L = int(input("please input L:",))
if L > length_window:
    print("Speech signal will lost")

data = np.append(data, np.zeros(length_window))
#print(type(data))
spectrum = fftpack.fft(data[0:length_window])
for n in range(L, sample_num, L):
    spectrum_in_window = fftpack.fft(data[n:n+length_window])
    spectrum = np.vstack((spectrum, spectrum_in_window))



data = np.array([])
for i in range(spectrum.shape[0]):
    data_in_window = fftpack.ifft(spectrum[i,:])[0:L]
    data = np.append(data, data_in_window)
#print(np.sum(np.round(data.real)))
data = np.round(data.real).astype(np.int32)
#print(data.sum())
#data = np.float64(np.round(data.real)))
#print(np.sum(data))

times = np.arange(len(data))/float(sample_rate)

plt.plot(times,data/32768)
plt.title('Speech Signal', fontsize = 18)
plt.xlabel('time',fontsize = 14)
plt.ylabel('amplitude',fontsize = 14)
plt.savefig('Signal_reconstruction.png')
wavfile.write("GFBS_DSP.wav", sample_rate, data)


