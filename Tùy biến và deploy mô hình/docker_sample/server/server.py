import io
from flask import Flask, Response, request, jsonify
from flask_cors import CORS
import torch
from model import CNN, transform_test
from PIL import Image

app = Flask(__name__)
CORS(app)

model = torch.load('./model.pth')
model.eval()

@app.route('/health', methods=['GET', 'POST'])
def health_check():
    return Response(status=200)

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return 'Hi!'

classes = {"0": "Mèo", "1": "Chó"}


def transform_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))

    return transform_test(image).unsqueeze(0)

def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return predicted_idx

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        predicted_idx= get_prediction(image_bytes=img_bytes)
        return jsonify({'predicted_idx': predicted_idx, "class": classes[predicted_idx]})

if __name__ == '__main__':
    app.run("0.0.0.0", 8000, debug=True)
