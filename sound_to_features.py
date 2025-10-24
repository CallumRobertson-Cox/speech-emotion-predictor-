import librosa
import numpy as np

def main(audio):
    pass

def sound_to_volume(audio):
    volume = librosa.feature.rms(y=audio)[0]
    return np.mean(volume)

def sound_to_pitch(audio):
    pitch = librosa.yin(y=audio, fmin=50, fmax=300)
    return np.mean(pitch)
    
def sound_to_tempo(audio):
    tempo, beats = librosa.beat.beat_track(y=audio)
    beat_times = librosa.frames_to_time(beats)
    beat_intervals = np.diff(beat_times)
    return float(tempo[0]), float(np.mean(beat_intervals))
    
#audio is the audio and sr is the sampling rate
audio,sr= librosa.load("C:/Users/callu/OneDrive/Documents/Sounds/Background.mp3")
