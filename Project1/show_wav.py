#!/usr/bin/python
from scipy.io import wavfile
from matplotlib import pyplot as plt
import numpy as np

# load the wav file and calculate the time 
sample_rate, data = wavfile.read('may_i_help.wav')
times = np.arange(len(data)/float(sample_rate))
print(data.shape)
# .ndim: Number of array dimensions
if data.ndim > 1:
    sample_num, channel_num = data.shape
else:
    channel_num = 1
    sample_num = data.shape[0]


