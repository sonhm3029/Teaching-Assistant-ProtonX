import streamlit as st
import requests
from PIL import Image

st.title("Cat or Dog Classifier")

# Input for Flask server URL
# server_url = st.text_input("Enter the Flask server URL", value="http://localhost:8000")

# File uploader for image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Send image to Flask server
    if st.button("Predict"):
        files = {"file": uploaded_file.getvalue()}
        try:
            response = requests.post("http://flask_server:8000/predict", files=files)
            if response.status_code == 200:
                result = response.json()
                st.success(f"Prediction: {result['class']}")
            else:
                st.error(f"Error {response.status_code}: Unable to get prediction")
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to connect to server: {e}")
