from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.sav', 'rb'))

# Mapping numeric classes to flower names
flower_names = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}

@app.route('/')
def home():
    return render_template('index.html', result='')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    result = ''
    try:
        # Get values from the form
        sepal_length = request.form.get('sepal_length', type=float)
        sepal_width = request.form.get('sepal_width', type=float)
        petal_length = request.form.get('petal_length', type=float)
        petal_width = request.form.get('petal_width', type=float)

        # Check if any value is missing or invalid
        if None in [sepal_length, sepal_width, petal_length, petal_width]:
            result = "Please provide valid values for all fields."
        else:
            # Use the model to predict
            prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
            flower = flower_names.get(prediction[0], "Unknown flower")
            result = f"{flower}"

    except Exception as e:
        result = f"Error: {str(e)}"

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
