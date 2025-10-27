from flask import Flask, request, jsonify, render_template_string
import librosa
import numpy as np
import tensorflow as tf
from get_features import get_features as get

app = Flask(__name__)

model = tf.keras.models.load_model("nn_emotion_model.keras")

emotion_map = {
    0: 'Neutral',
    1: 'Calm',
    2: 'Happy',
    3: 'Sad',
    4: 'Angry',
    5: 'Fearful',
    6: 'Disgust',
    7: 'Surprised'
}

def prepare_features(y, sr):
    features = get(y,sr)
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
    return row_data


@app.route("/")
def index():
    # Simple HTML form
    return render_template_string("""
        <!doctype html>
        <title>Emotion Predictor</title>
            <style>
                h1 {color: darkred; }     
            </style>
        <h1>Upload a WAV file</h1>
        <form action="/predict" method="post" enctype="multipart/form-data">
            <input type="file" name="file" accept="audio/* capture="microphone">
            <input type="submit" value="Upload/Record">
        </form>
    """)


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "no file"})
    
    file = request.files['file']
    y, sr = librosa.load(file, sr=None)

    row_data = prepare_features(y,sr)

    if row_data is None or row_data.size == 0:
        raise ValueError("Feature extraction failed — row_data is empty or None")

    if model is None:
        raise ValueError("Model failed to load — check file path and format")

    print("Row data shape:", row_data.shape)

    prediction = model.predict(row_data)[0]

    predicted_class = int(np.argmax(prediction))
    return jsonify({
        'emotion': emotion_map[predicted_class],
        'probabilities': prediction.tolist()
    })

if __name__ == '__main__':
    app.run(debug=True)