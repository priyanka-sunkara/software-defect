from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load the trained Naive Bayes model
try:
    with open('C:\Users\Priyanka\Downloads\Project\software-defect\naive_bayes_model.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    print(f"Error loading model: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from the form
        loc = float(request.form['loc'])
        v_g = float(request.form['v(g)'])
        ev_g = float(request.form['ev(g)'])
        iv_g = float(request.form['iv(g)'])
        n = float(request.form['n'])
        v = float(request.form['v'])
        l = float(request.form['l'])
        d = float(request.form['d'])
        i = float(request.form['i'])
        e = float(request.form['e'])
        b = float(request.form['b'])
        t = float(request.form['t'])
        lOCode = float(request.form['lOCode'])
        lOComment = float(request.form['lOComment'])
        lOBlank = float(request.form['lOBlank'])
        locCodeAndComment = float(request.form['locCodeAndComment'])
        uniq_Op = float(request.form['uniq_Op'])
        uniq_Opnd = float(request.form['uniq_Opnd'])
        total_Op = float(request.form['total_Op'])
        total_Opnd = float(request.form['total_Opnd'])
        branchCount = float(request.form['branchCount'])
        # Add more features as needed

        # Make prediction using the loaded model
        features = [loc, v_g, ev_g, iv_g, n, v, l, d, i, e, b, t, lOCode, lOComment, lOBlank, locCodeAndComment, uniq_Op, uniq_Opnd, total_Op, total_Opnd, branchCount]
        prediction = model.predict([features])

        # Return the prediction result as JSON
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
