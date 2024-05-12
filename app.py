from flask import Flask,request
import pickle
import pandas as pd
import numpy as np


app = Flask(__name__)
pickle_in = open("classfier.pkl","rb")
classfier=pickle.load(pickle_in)

@app.route('/')  
def welcome():
    return 'welcome'

@app.route('/pred')
def predict_note_Authenication():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    predication = classfier.predict([[variance,skewness,curtosis,entropy]])
    return "The Predict Value is " + str(predication)


@app.route('/pred_file',methods=['post'])
def predict_note():
    df_test = pd.read_csv(request.files.get('file'))
    predication = classfier.predict(df_test)
    return "The Predict Value is " + str(list(predication))

if __name__ == '__main__':
    app.run()
