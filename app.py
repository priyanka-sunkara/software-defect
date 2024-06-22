from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)  # Correct initialization of the Flask application

# Load the trained Naive Bayes model
with open('naive_bayes_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(request.form['feature1']), float(request.form['feature2'])]
    # Add more features as needed
    prediction = model.predict([features])
    return jsonify({'prediction': int(prediction[0])})

if _name_ == '_main_':
    app.run(debug=True)

