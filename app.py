from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Your feature-dependent Naive Bayes model (replace with your actual model)
def predict_defect(loc, v_g, lOCode):
    # Your prediction logic here
    # Example: return 1 if defect, else return 0
    return 1

@app.route('/')
def index():
    return ('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    loc = float(request.form['loc'])
    v_g = float(request.form['v(g)'])
    lOCode = float(request.form['lOCode'])

    # Call your prediction function
    prediction = predict_defect(loc, v_g, lOCode)

    # Redirect to a new page to display the result
    return redirect(url_for('result', prediction=prediction))

@app.route('/result/<int:prediction>')
def result(prediction):
    return ('result.html', prediction=prediction) # type: ignore

if __name__ == '__main__':
    app.run(debug=True)
