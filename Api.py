from flask import Flask,request
import pandas as pd
import csv
import numpy as np
from flask_cors import CORS
import json 

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/post', methods=['POST'])
 
def post():
    result={}  
    file = request.files['file']

    df=pd.read_csv(file , delimiter=',', names=['DATE','MODE','PARTICULARS','DEPOSITS','WITHDRAWALS','BALANCE']) 
    result["name"] = df.loc[df.index[0], 'DATE']
    result["street"] = df.loc[df.index[1], 'DATE']
    result["area"] = df.loc[df.index[2], 'DATE']
    result["city"] = df.loc[df.index[3], 'DATE']
    result["state"] = df.loc[df.index[4], 'DATE']
    result["document"] = df.loc[df.index[10], 'DATE']
    result["details"] = df.loc[df.index[16], 'DATE']

    transactionList=[]
    temp={}
    i=0
    j=0
    for index,x in df.iloc[18:len(df.index)].iterrows():
        if(i!=0):
            temp={'date':x['DATE'],'mode':x['MODE'],'particulars':x['PARTICULARS'],'deposits':x['DEPOSITS'],'withdrawals':x['WITHDRAWALS'],'balance':x['BALANCE']}
            transactionList.insert(j,temp)
            j=j+1
        i=i+1
    temp={}
    result["TransactionList"] = transactionList
    
    return json.dumps(result).replace("NaN", u'""')

if __name__=="__main__":
    app.run(debug=True)