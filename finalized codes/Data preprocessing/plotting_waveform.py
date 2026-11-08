#plotting waveform
import librosa, librosa.display
import matplotlib.pyplot as plt

file="C:/Users/Hams R/OneDrive/Documents/internaudio/AnkitMandal_1.mp3"
#waveform
signal, sr=librosa.load(file,sr=22050)    #sr*t= 22050*30         
#22050 is the librosa standard resampling rate while loading a file.

plt.plot(signal)
plt.title('Audio Signal Waveform')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()