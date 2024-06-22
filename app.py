from io import SEEK_CUR
from typing import TypeVar
from flask import Flask, request, jsonify
from flask.scaffold import F
import pickle

from sklearn import model_selection
T = TypeVar("T", model_selection, SEEK_CUR)

app = Flask(__name__)

# Load the trained Naive Bayes model
try:
    with open('naive_bayes_model.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    print(f"Error loading model: {e}")
    F .seek(0)

@app.route('/')
def home():
    return ('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from the form
        features = [float(request.form['feature1']), float(request.form['feature2'])]
        # Add more features as needed

        # Make prediction using the loaded model
        prediction = model.predict([features])
        
        # Return the prediction result as JSON
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)