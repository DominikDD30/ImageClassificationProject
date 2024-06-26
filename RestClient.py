import os
import cv2
import numpy as np
from flask import Flask, request, jsonify
from PIL import Image
from flask_cors import CORS
from tensorflow.keras.models import load_model

app = Flask(__name__)
CORS(app)
model = load_model(os.path.join('models', 'binaryV2_20e.h5'))

def preprocess_image(image, target_size=(150, 150)):
    # Convert image to RGB if it has an alpha channel
    if image.shape[2] == 4:  # Check if image has an alpha channel
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    img = cv2.resize(image, target_size)
    img = np.array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0
    return img

def predict_single_image(image):
    img = preprocess_image(image)

    result = model.predict(img)[0][0]
    result = float(result)
    print(f"Raw prediction output: {result}")

    if result > 0.5:
        return {"class": 'R', "value": result}
    else:
        return {"class": 'O', "value": result}


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        img = Image.open(file).convert('RGB')
        img = np.array(img)
        prediction = predict_single_image(img)

        return jsonify(prediction), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
