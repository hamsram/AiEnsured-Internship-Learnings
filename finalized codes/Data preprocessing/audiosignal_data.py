#plotting waveform
#When the file is loaded, it is decompressed and converted into a Numpy array.

import librosa, librosa.display

file="C:/Users/Hams R/OneDrive/Documents/internaudio/AnkitMandal_1.mp3"

signal, sr=librosa.load(file,sr=22050)    #sr*t= 22050*30         
#22050 is the librosa standard resampling rate while loading a file.

print ('Example shape ', signal.shape, 'Sample rate ', sr, 'Data type', type(signal))
print (signal[22400:22420])