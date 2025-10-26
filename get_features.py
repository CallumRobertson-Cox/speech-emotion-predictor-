import librosa
import numpy as np

# def sound_to_volume(audio, sr):
#     volume = librosa.feature.rms(y=audio)[0]
#     return float(np.std(volume))

# def sound_to_pitch(audio, sr):
#     pitch = librosa.yin(y=audio, fmin=50, fmax=300, sr=sr)
#     return float(np.std(pitch))
    
# def sound_to_tempo(audio, sr):
#     tempo, beats = librosa.beat.beat_track(y=audio, sr =sr)
#     beat_times = librosa.frames_to_time(beats)
#     beat_intervals = np.diff(beat_times)
#     return float(tempo[0]), float(np.std(beat_intervals))

# def sound_to_ZCR(audio, sr):
#     ZCR = librosa.feature.zero_crossing_rate(y=audio)[0]
#     return float(np.std(ZCR))

# def get_features(audio, sr):
#     vol = sound_to_volume(audio, sr)
#     pitch = sound_to_pitch(audio, sr)
#     tempo, beats = sound_to_tempo(audio, sr)
#     ZCR = sound_to_ZCR(audio, sr)

#     return dict({
#         "volume" : vol,
#         "pitch" : pitch,
#         "tempo" : tempo,
#         "beats" : beats,
#         "ZCR" : ZCR
#     })


def get_features(y,sr):
    features = {
        'mfcc_mean': np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13), axis=1),
        'mfcc_std': np.std(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13), axis=1),
        'chroma_mean': np.mean(librosa.feature.chroma_stft(y=y, sr=sr), axis=1),
        'spectral_contrast_mean': np.mean(librosa.feature.spectral_contrast(y=y, sr=sr), axis=1),
        'tonnetz_mean': np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(y), sr=sr), axis=1),
        'zcr_mean': np.mean(librosa.feature.zero_crossing_rate(y)),
        'rms_mean': np.mean(librosa.feature.rms(y=y)),
        'pitch_mean': np.mean(librosa.piptrack(y=y, sr=sr)[0])
    }

    print(features)
    return dict(features)