import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np
file = "C:/Users/Hams R/OneDrive/Documents/internaudio/AnkitMandal_1.mp3"
signal, sr = librosa.load(file, sr=22050)  # sr*t = 22050*30

n_fft = 2048  # no of samples
# amount of shifting each ft towards the right
hop_len = 512

# extracting the short time fourier transform
stft = librosa.core.stft(signal, hop_length=hop_len, n_fft=n_fft)

# getting the magnitude from complex data
spectrogram = np.abs(stft)
log=librosa.amplitude_to_db(spectrogram)
# calculating MFCCs
n_mfcc = 13
mfcc = librosa.feature.mfcc(S=log, n_mfcc=13)
plt.figure(figsize=(14, 7))
librosa.display.specshow(mfcc, sr=sr, hop_length=hop_len, x_axis='time')
plt.colorbar()
plt.title('MFCC')
plt.show()
