from flask import Flask, request, jsonify, render_template
import pickle
import logging

app = Flask(__name__)

# Load the trained Naive Bayes model
try:
    with open('naive_bayes_model.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    logging.error(f"Error loading model: {e}")
    raise  # Reraise the exception for debugging

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from the form
        feature1 = float(request.form.get('feature1'))
        feature2 = float(request.form.get('feature2'))
        # Add more features as needed

        # Validate input (example: check if features are within a valid range)
        if not (0 <= feature1 <= 10 and 0 <= feature2 <= 10):
            return jsonify({'error': 'Invalid input. Features must be between 0 and 10.'}), 400

        # Make prediction using the loaded model
        prediction = model.predict([[feature1, feature2]])

        # Return the prediction result as JSON
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
   
