import numpy as np
from matplotlib import pyplot as plt
from scipy import fftpack
from scipy.io import wavfile
import dTDFT


sample_rate, data = dTDFT.sample_rate, dTDFT.data
sample_num = dTDFT.sample_num
length_window = dTDFT.length_window
L = dTDFT.L
spectrum = dTDFT.spectrum
print(spectrum.shape)
data = np.array([])
for i in range(spectrum.shape[0]):
    data_in_window = fftpack.ifft(spectrum[i,:])[0:L]
    data = np.append(data, data_in_window)
print(data.shape)
data = np.int16(np.round(data.real))

times = np.arange(len(data))/float(sample_rate)
#print(times)
#time = np.arange(len(data)/float(sample_rate))
#print(time)
plt.plot(times,data/32768)
plt.title('Speech Signal', fontsize = 18)
plt.xlabel('time',fontsize = 14)
plt.ylabel('amplitude',fontsize = 14)
plt.savefig('Signal_reconstruction.png')
print(sample_rate)
print(data)
wavfile.write("GFBS_DSP.wav", sample_rate, data)


