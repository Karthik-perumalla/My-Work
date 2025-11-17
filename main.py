#libraries used
from flask_sqlalchemy import SQLAlchemy, session
from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, relationship
from datetime import datetime
import os
import json
from flask import make_response
from flask_restful import Resource, Api, fields, marshal_with, reqparse
from werkzeug.exceptions import HTTPException
import re
import joblib

app = Flask(__name__)

api = Api(app)
app.app_context().push()


def predict(arr):
    loaded_knn = joblib.load('knn_model.joblib')
    ans=loaded_knn.predict([arr])
    print("called: ",ans)
    return ans
# Account length,International plan,Voice mail plan,Number vmail messages,Total day minutes,Total day calls,Total day charge,Total eve minutes,Total eve calls,Total eve charge,Total night minutes,Total night calls,Total night charge,Total intl minutes,Total intl calls,Total intl charge,Customer service calls

@app.route('/', methods=["GET", "POST"])
def AdminLogin():
    if request.method == "GET":
        return render_template("home.html",ans)
    
    try:
        # Gather and validate inputs
        fields = [
            'Account_length', 'International_plan', 'Voice_mail_plan',
            'Number_vmail_messages', 'Total_day_minutes', 'Total_day_calls',
            'Total_day_charge', 'Total_eve_minutes', 'Total_eve_calls',
            'Total_eve_charge', 'Total_night_minutes', 'Total_night_calls',
            'Total_night_charge', 'Total_intl_minutes', 'Total_intl_calls',
            'Total_intl_charge', 'Customer_service_calls'
        ]
        arr = [float(request.form[field]) for field in fields]
        
        # Predict
        ans = predict(arr)
        return render_template("home.html", ans=ans)
    
    except Exception as e:
        return make_response(f"Error: {str(e)}", 400)


if (__name__) == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)