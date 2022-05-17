import flask
from flask import Flask, jsonify, request, render_template, request, redirect, url_for
import json 
import pickle
import numpy as np
import pandas as pd

from data_input import data_in

#Method to load model into the app
def load_models():
    file_name = 'models/model_file.p'
    
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

#Method to load the scaler into the app
def load_scaler():
    file_name = 'models/scaler.pkl'
    
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        scaler = data['scaler']
    return scaler

#Method to make a prediction on a sample of data
app = Flask(__name__)
@app.route('/predict', methods=['GET'])
def predict(sample):
    
    #stub inputs
    #x = np.array(data_in).reshape(1, -1)
    #request_json = request.get_json()
    #x = request_json['input']
    
    
    #x_in = np.array(x).reshape(1, -1)
    #load model
    model = load_models()
    #prediction = model.predict(x_in)[0]
    
    prediction = model.predict(sample)
    
    #response = json.dumps({'response': prediction})
    
    #return response, 200
    
    return prediction

#Render the homepage of the app where a form is submitted
@app.route('/')
def home():
    return render_template('index.html')

#Format the form submission into a data sample for the model to make a prediction, then return the result page
@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        
        scaler = load_scaler()
        
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        brand_number = int(to_predict_list[0])
        remaining_vars = to_predict_list[1:]
        
        #Transforming dummy variable columns
        brand_idx = brand_number
        brand_dummies = [0] * 14
        brand_dummies[brand_idx] = 1
        
        #Transforming and scaling sample values to make accurate predictions
        remaining_vars = list(map(float, remaining_vars))
        
        final_pred_list = brand_dummies + remaining_vars        
        idx_to_log = [0,1,2,3,4,5,7,8,9,10,11,12,13]
        
        #Performing data transformations and scaling the sample data
        for idx in idx_to_log:
            final_pred_list[idx] = np.log1p(final_pred_list[idx])
        
        final_pred_list_scaled = scaler.transform(np.array(final_pred_list).reshape(1, -1))
        
        print(final_pred_list_scaled)
        
        print('check it out: ')
        
        #Format the string output and return the resulting prediction
        prediction = '$'+str(round(predict(final_pred_list_scaled)[0], 2))
        
        print(prediction)
        
        return render_template('result.html', prediction = prediction)
        
        
                
if __name__ == '__main__':
    app.run(debug=True)
    
    
