import librosa
import numpy as np

def sound_to_volume(audio, sr):
    volume = librosa.feature.rms(y=audio)[0]
    return float(np.mean(volume))

def sound_to_pitch(audio, sr):
    pitch = librosa.yin(y=audio, fmin=50, fmax=300, sr=sr)
    return float(np.mean(pitch))
    
def sound_to_tempo(audio, sr):
    tempo, beats = librosa.beat.beat_track(y=audio, sr =sr)
    beat_times = librosa.frames_to_time(beats)
    beat_intervals = np.diff(beat_times)
    return float(tempo[0]), float(np.mean(beat_intervals))

def sound_to_ZCR(audio, sr):
    ZCR = librosa.feature.zero_crossing_rate(y=audio)[0]
    return float(np.mean(ZCR))

def get_features(audio, sr):
    vol = sound_to_volume(audio, sr)
    pitch = sound_to_pitch(audio, sr)
    tempo, beats = sound_to_tempo(audio, sr)
    ZCR = sound_to_ZCR(audio, sr)

    return dict({
        "volume" : vol,
        "pitch" : pitch,
        "tempo" : tempo,
        "beats" : beats,
        "ZCR" : ZCR
    })

