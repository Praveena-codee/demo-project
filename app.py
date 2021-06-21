###### # ##import necessary libraries

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    url_for)

import os
import numpy as np
import random, json
import joblib
import pickle


import sys
import numpy as np


######## creating and connecting flask

app = Flask(__name__)



###create route that renders index.html template

@app.route('/')
def home():
    return render_template("Page-1.html")
    #return "Hi"

@app.route('/Home.html')
def Home_webpage():
    return render_template("Home.html")  

@app.route('/data.html')
def graph_webpage():
    return render_template("tableau.html")  

@app.route('/form.html', methods=["POST", "GET"])
def form():

    return render_template("form.html")  



# @app.route("/result.html", methods=["GET", "POST"])
# def result():
    # handle the POST request
    # if request.method == 'POST':
    #     devices_count = request.args.get('devices_count')
    #     usage = request.args.get('usage')
    #     rate = request.args.get('rate')
    #     return'''
    #             <h1>Please reduce your devices in Bedroom: {}</h1>
    #             <h1> Please monitor your usage: {}</h1>
    #             <h1> Have a great day tomorrow: {}</h1>'''.format(devices_count, usage, rate)

    # # otherwise handle the GET request
    # return '''
    #        <form method="POST">
         
    #            <input type="submit" value="Submit">
    #        </form>'''




@app.route("/result.html", methods=["GET", "POST"])
def result():
    if request.method == 'POST':
        
        devices_count = request.args.get('devices_count')
        #usage = request.args.get('usage')
        rate=request.args.get('rate')
        #return'''
            
           # <h1> Have a great day tomorrow: {}</h1>'''.format(rate)
    # print(rate)
    #sleeprate = (int(rate) < 9)? "bad sleep":"good sleep";
    devices_count = request.args.get('devices_count')
    rate=request.args.get('rate') 
    
    #usage = request.args.get('usage')
    if(int(rate) < 6 and int(devices_count) > 6 ):
	    
        rate="bad sleep - catch up"
        
    
    elif (int(rate) > 6 and int(devices_count) < 3):
	    rate="good sleep - Well Done"
	
    else:
	    rate="ok sleep - health is wealth"

    return '''
        <div style="background-color: white;"> 
         <h1> "Sleep Analysis Prediction": {}</h1></div>'''.format(rate)
         
	
       
        
    
    
    
     # otherwise handle the GET request
    # return '''
    #     <form method="POST">
    #         <input type="submit" value="Submit">
    #             </form>'''    
    # #return.format(rate)
    #return render_template("result.html")  

              
    # {% if (rate > 9) %}
    #     <h1>  -> RPM:,ECT:{{VAL.ECT}} <button type="button" class="btn  btn-danger btn-sm">High</button> </h1>
    # {% else %}
    #     <p> {{VAL.Count}} -> RPM:{{VAL.RPM}},ECT:{{VAL.ECT}} <button type="button" class="btn btn-success btn-md">Normal</button> </p>
    # {% endif %}
    


    
        

    # if request.method == "POST":
    #     activities = request.form["activities"]
    #     devicesBR = request.form["devicesBR"]
    #     devices_count = request.form["devices_count"]
    #     usage = request.form["usage"]
    #     Rules = request.form["Rules"]
    #     enforce = request.form["enforce"]
    #     behaviour = request.form["behaviour"]
    #     rate = request.form["rate"]

    #     storedModel = joblib.load("sleep_analysis.ml")
    #     storedScaler = joblib.load("sleep_analysis.ml")

    #     prediction = [[activities,devicesBR,devices_count,usage,Rules,enforce,behaviour,rate]]

    #     scaled_prediction = storedScaler.transform(prediction)
    #     p = storedModel.predict(scaled_prediction)

    #     def result(prediction):
    #         result = 'good'
    #         if prediction[0] == 1:
    #             result = 'bad'
    #         return result   

    #     outcome = result(p)
        
    #     print(outcome)
    














    
# if __name__ == "__main__":
#     app.run()
   
if __name__ == "__main__":
    app.run(port=5001, debug=True)