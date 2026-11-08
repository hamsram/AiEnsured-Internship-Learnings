import librosa
import numpy as np
import matplotlib.pyplot as plt

audio_file = "C:/Users/Hams R/OneDrive/Documents/internaudio/AnkitMandal_1.mp3"
x, sr = librosa.load(audio_file, sr=None)
print(x.shape, sr)

plt.figure()
plt.plot(np.arange(len(x)) / sr, x)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.show()
