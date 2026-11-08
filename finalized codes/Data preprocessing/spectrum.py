import librosa, librosa.display
import matplotlib.pyplot as plt

file="C:/Users/Hams R/OneDrive/Documents/internaudio/AnkitMandal_1.mp3"
signal, sr=librosa.load(file,sr=22050)    #sr*t= 22050*30

#fft-spectrum
import numpy as np
fft=np.fft.fft(signal)
magnitude=np.abs(fft)
frequency=np.linspace(0,sr,len(magnitude))  #evenly spaced numbers
left_frequency=frequency[:int(len(frequency)/2)]
left_magnitude=magnitude[:int(len(magnitude)/2)]
plt.plot(left_frequency, left_magnitude)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()







"""n_fft=2048   #no of samples
hop_len=512
stft=librosa.core.stft(signal,hop_length=hop_len, n_fft=n_fft)
spectogram=np.abs(stft)
librosa.display.specshow(spectogram,sr=sr,hop_length=hop_len)
plt.xlabel("time")
plt.ylabel("frequency")
plt.colorbar()
plt.show()"""