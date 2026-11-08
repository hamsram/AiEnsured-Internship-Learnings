import librosa
import soundfile as sf

audio_file = "C:/Users/Hams R/Downloads/Aastha_1.m4a"
audio, sr = librosa.load(audio_file, sr=None)  # Load audio file with its sampling rate

segment_duration = 1.0  # Duration of each segment in seconds
segment_samples = int(segment_duration*sr)  # multiply segment duration by sr to Convert segment duration to samples

segments = []
for i in range(0, len(audio), segment_samples):
    segment = audio[i:i + segment_samples]
    segments.append(segment)

for i, segment in enumerate(segments):
    output_file = f'Aastha_1_{i+1}.wav'
    sf.write(output_file, segment, sr)

