import librosa
import soundfile as sf
import os
def trim(audio_file,segment_duration,filename):
    audio, sr = librosa.load(audio_file, sr=None)  # Load audio file with its sampling rate
    trimmed, _ = librosa.effects.trim(audio)
    print(librosa.get_duration(y=audio,sr=sr),librosa.get_duration(y=trimmed,sr=sr))        #to check the duration of trimmed vs actual file   
    segment_samples = int(segment_duration*sr)  # multiply segment duration by sr to Convert segment duration to samples
    segments = []
    for i in range(0, len(trimmed), segment_samples):
        segment = trimmed[i:i + segment_samples]
        segments.append(segment)
    for i, segment in enumerate(segments):
        output_file = f'{filename}_{i+1}.wav'
        sf.write(output_file, segment, sr)
dirname ="C:/Users/Hams R/Documents/internship/All audio files"     # Directory name
ext = '.wav'    # File extension
segment_duration=3.0
for files in os.listdir(dirname):      # Iterating over all files
    if files.endswith(ext):
        file_path = os.path.join(dirname, files)         #
        filename = os.path.splitext(files)[0]            #only name of file without extension
        trim(file_path,segment_duration,filename)        #calling the function
        print(filename)  





