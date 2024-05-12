from flask import Flask,request
import pickle
import pandas as pd
import numpy as np
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

pickle_in = open("classfier.pkl","rb")
classfier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return 'welcome'

@app.route('/pred')
def predict_note_Authenication():
    """Let's Authenicate the Banks Note
    This is usinge docstring for specification
    ---
    parameters:
        -  name: variance
           in: query
           type: number
           required: True
        -  name: skewness
           in: query
           type: number
           required: True
        -  name: curtosis
           in: query
           type: number
           required: True
        -  name: entropy
           in: query
           type: number
           required: True
    responses:
        200:
            description: The output values
    """
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    predication = classfier.predict([[variance,skewness,curtosis,entropy]])
    return "The Predict Value is " + str(predication)



@app.route('/pred_file',methods=['post'])
def predict_note():
    """Let's Authenicate the Banks Note
    This is usinge docstring for specification
    ---
    parameters:
        -  name: file
           in:  formdata
           type: file
           required: true
    responses:
        200:
            description: The output valuse
    """
    df_test = pd.read_csv(request.files.get('file'))
    predication = classfier.predict(df_test)
    return "The Predict Value is " + str(list(predication))
if __name__ == '__main__':
    app.run()
