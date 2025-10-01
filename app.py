#importing flask 
from flask import Flask,request,render_template
import pandas as pd
import pickle
import os
from CustomEncoder import FrequencyEncoder
import sklearn
import imblearn

churn_pred_model=pickle.load(open('my_ml_pipeline','rb'))

#Initialize the Flask app
app = Flask(__name__,template_folder = 'templates')
 

#Setting up the main route
@app.route('/',methods=['GET','POST'])  

def predict_churn():
    if request.method == 'GET':
        return(render_template('churn.html')) #render initial form to get input
    
    if request.method == 'POST':
        #get input
        Contract = request.form['Contract']
        Tenure = request.form['Tenure']
        InternetService = request.form['InternetService']
        TotalCharges = request.form['TotalCharges']
        PaymentMethod = request.form['PaymentMethod']
        MonthlyCharges = request.form['MonthlyCharges']
        TechSupport = request.form['TechSupport']
    
    #Dataframe for the model
    test=pd.DataFrame([[Contract,Tenure,InternetService,TotalCharges,PaymentMethod,MonthlyCharges,TechSupport]],
                      columns=['Contract','Tenure','InternetService','TotalCharges','PaymentMethod','MonthlyCharges','TechSupport'],
                      index=['input'])

    #model prediction
    prediction=churn_pred_model.predict(test)[0]
    
    return render_template('churn.html',
                                 original_input={'Contract':Contract,
                                                 'Tenure':Tenure,
                                                 'InternetService':InternetService,
                                                 'TotalCharges':TotalCharges,
                                                 'PaymentMethod':PaymentMethod,
                                                 'MonthlyCharges':MonthlyCharges,
                                                 'TechSupport':TechSupport},
                                 result=prediction,
                                 )
    
    

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000)) #defining port to map container port to local host
    app.run(host='0.0.0.0',port=port)