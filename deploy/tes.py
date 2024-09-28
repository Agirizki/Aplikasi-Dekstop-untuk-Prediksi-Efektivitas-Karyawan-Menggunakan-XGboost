# Import Library
from flask import Flask, render_template, jsonify, request
from joblib import load
import numpy as np
import pickle
import pandas as pd



app = Flask(__name__)
model = pickle.load(open('model_faktor_efektivitas_karyawan.pkl', 'rb'))


@app.route('/slider')
def index():
    return render_template("Slider.html")

@app.route('/about')
def about():
    return render_template("biodata.html")

@app.route('/')
def beranda():
    return render_template('kelompok1.html')

@app.route('/predict', methods = ['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    output = 2
    output = round(prediction[0], 2)

    return render_template("Slider.html", prediction_text=output)

'Ya/Tidak[1/0] :{}'

    

if __name__ == '__main__':
    app.run(debug=True)