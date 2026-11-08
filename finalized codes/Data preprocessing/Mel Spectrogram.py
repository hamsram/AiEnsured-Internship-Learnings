#mel spectogram plotting
import matplotlib.pyplot as plt
import librosa, librosa.display


file="C:/Users/Hams R/OneDrive/Documents/internaudio/AnkitMandal_1.mp3"
signal, sr=librosa.load(file,sr=22050)    #sr*t= 22050*30

#fft-spectrum
import numpy as np
#stft- spectogram
n_fft=2048   #no of samples
#amount of shifting each ft towards right
hop_len=512   

#extracting the short time fourier transform
stft=librosa.core.stft(signal,hop_length=hop_len, n_fft=n_fft)  

#getting the magnitude from complex data
spectogram=np.abs(stft)  

librosa.display.specshow(spectogram,sr=sr,hop_length=hop_len)
plt.xlabel("time")
plt.ylabel("frequency")
plt.colorbar()
plt.show()



