import matplotlib.pyplot as plt
import librosa
import librosa.display

file = "C:/Users/Hams R/OneDrive/Documents/internaudio/AnkitMandal_1.mp3"
signal, sr = librosa.load(file, sr=22050)  # sr*t = 22050*30

# fft-spectrum
import numpy as np

# stft- spectrogram
n_fft = 2048  # no of samples
# amount of shifting each ft towards the right
hop_len = 512

# extracting the short time fourier transform
stft = librosa.core.stft(signal, hop_length=hop_len, n_fft=n_fft)

# getting the magnitude from complex data
spectrogram = np.abs(stft)

plt.figure(figsize=(10, 4))
librosa.display.specshow(librosa.amplitude_to_db(spectrogram, ref=np.max), sr=sr, hop_length=hop_len, x_axis='time', y_axis='linear')
#plt.colorbar(format='%+2.0f dB')
plt.title('Mel Spectrogram')
#plt.tight_layout()
plt.show()
