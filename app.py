# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the CLassifier model
filename = 'heart-disease-prediction-model.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('main.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        # Convert form inputs to appropriate data types
        age = int(request.form['age'])
        sex = int(request.form['sex'])  # Convert to int
        cp = int(request.form['cp'])  # Convert to int
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = int(request.form['fbs'])  # Convert to int
        restecg = int(request.form['restecg'])
        thalach = int(request.form['thalach'])
        exang = int(request.form['exang'])  # Convert to int
        oldpeak = float(request.form['oldpeak'])
        slope = int(request.form['slope'])  # Convert to int
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])  # Convert to int
        
        # Create a numpy array with the converted values
        data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        # Make prediction
        my_prediction = model.predict(data)
        
        return render_template('result.html', prediction=my_prediction)
    else:
        return render_template('predict.html')

@app.route('/about')
def about():
    return render_template('about.html')      

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission for contact
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
    
        return redirect(url_for('contact_success'))
    else:
        return render_template('contact.html')

@app.route('/contact/success')
def contact_success():
    return render_template('contact_success.html')
        

if __name__ == '__main__':
	app.run(debug=True)

