#finalized code
import os
import librosa
import soundfile as sf
from scipy import signal
def data_cleaning(input_file, output_file, final_sample_rate):
    audio, original_sample_rate = librosa.load(input_file, sr=None)
    trimmed, _ = librosa.effects.trim(audio)
    resampled_audio = signal.resample(trimmed, int(len(trimmed) * final_sample_rate / original_sample_rate))
    normalized_audio = librosa.util.normalize(resampled_audio)
    sf.write(output_file, normalized_audio, final_sample_rate)

def iterate(directory):
    for filename in os.listdir(directory):
        input_path = os.path.join(directory, filename)
        if os.path.isfile(input_path):           
            output_path=f'C:/Users/Hams R/OneDrive/Documents/cleaned_files2/cleaned{filename}'
            data_cleaning(input_path, output_path, final_sample_rate)
            print(f"Cleaned- {input_path} and added to {output_path}")

directory_path = "C:/Users/Hams R/OneDrive/Documents/internaudio"

final_sample_rate = 44100      
#44100  is the standard for high quality audio storage

iterate(directory_path)
