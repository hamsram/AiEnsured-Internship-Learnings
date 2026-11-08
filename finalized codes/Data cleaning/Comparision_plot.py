#Comparison plots for cleaned audio data vs original audio
import librosa
import matplotlib.pyplot as plt

def plot_audio_comparison(actual_audio, modified_audio, samplerate):
    # Time axis for both the audio signals
    actual_time = librosa.times_like(actual_audio, sr=samplerate)
    modified_time = librosa.times_like(modified_audio, sr=samplerate)

    # 2 rows and 1 column passed as parameter to plt.subplots()
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True,figsize=(20, 7))        #sharex used to share x axis between both the plots

    # Plot the original audio file waveform
    ax1.plot(actual_time, actual_audio, label='Original Audio', color='b')
    ax1.set_title('Original Audio ')
    ax1.set_ylabel('Amplitude')

    # Plot the modified audio file waveform
    ax2.plot(modified_time, modified_audio, label='Modified Audio', color='r')
    ax2.set_title('After applying data cleaning techniques')
    ax2.set_xlabel('Time in seconds')
    ax2.set_ylabel('Amplitude')
    plt.show()


actual_audio, original_samplerate = librosa.load("C:/Users/Hams R/OneDrive/Documents/internaudio/AnkitMandal_1.mp3", sr=None)
modified_audio, modified_samplerate = librosa.load("C:/Users/Hams R/OneDrive/Documents/cleaned_files2/cleanedAnkitMandal_1.mp3", sr=None)


plot_audio_comparison(actual_audio, modified_audio, original_samplerate)
