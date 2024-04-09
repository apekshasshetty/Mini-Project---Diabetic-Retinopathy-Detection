import os
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.inception_v3 import preprocess_input
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the machine learning model
model = load_model("IBMDR.h5")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about_us():
    return render_template('about.html')

@app.route('/index')
def index_page():
    return render_template('index.html')

@app.route('/result', methods=["POST"])
def res():
    if request.method == "POST":
        f = request.files['image']
        basepath = os.path.dirname(__file__)
        filepath = os.path.join(basepath, 'uploads', f.filename)
        f.save(filepath)

        # Load and preprocess the image for prediction
        img = image.load_img(filepath, target_size=(299, 299))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        img_data = preprocess_input(x)

        # Make prediction using the loaded model
        prediction = np.argmax(model.predict(img_data), axis=1)

        # Define the classes
        index = ['No Diabetic Retinopathy', 'Mild DR', 'Moderate DR', 'Severe DR', 'Proliferative DR']
        result = index[prediction[0]]

        return render_template('prediction.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True,port=5001)
