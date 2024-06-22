from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load the trained Naive Bayes model
try:
    with open('naive_bayes_model.pkl' , 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    print(f"Error loading model: {e}")

@app.route('/')
def home():
    return('index.html')

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

if __name__ == '_main_':
    app.run(debug=True)