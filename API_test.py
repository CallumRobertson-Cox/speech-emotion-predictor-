import requests
import sounddevice as sd 
from scipy.io.wavfile import write 
import os
from get_features import get_features as get
import librosa
import pandas as pd 
import tensorflow as tf
import numpy as np
import time

def predict(features):

    row_data = []

    row_data += [features['zcr_mean']]
    row_data += [features['rms_mean']]
    row_data += [features['pitch_mean']]
    row_data += [1]

    row_data += list(features['mfcc_mean'])
    row_data += list(features['mfcc_std'])
    row_data += list(features['chroma_mean'])
    row_data += list(features['spectral_contrast_mean'])
    row_data += list(features['tonnetz_mean'])

    row_data = np.array(row_data, dtype=np.float32).reshape(1,-1)

    model = tf.keras.models.load_model('nn_emotion_model.keras')
    prediction = model.predict(row_data).astype(float).tolist()

    emotion_map = {
    0: "neutral",
    1: "calm",
    2: "happy",
    3: "sad",
    4: "angry",
    5: "fearful",
    6: "disgust",
    7: "surprised"
}

    for i in range(8):
        if prediction[0][i] == 1:
            print(prediction)
            return emotion_map[i]

def voice_input():
    print("Recording ...")
    sample_rate = 44100
    duration = 5
    audio = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=1)
    time.sleep(5)
    sd.wait()
    write("output.wav", sample_rate, audio)
    print('saved as output.wav')

    y,sr = librosa.load('output.wav',sr=None)

    print("Processing ...")

    features = get(y,sr)
    print(predict(features))

    
voice_input()