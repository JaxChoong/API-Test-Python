from flask import Flask, request, jsonify,render_template,redirect,url_for
import requests
from dotenv import load_dotenv
import os
import functions as f
import json
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart




app = Flask(__name__)

CORS(app)
load_dotenv()

API_KEY = os.getenv('API_KEY')

@app.route('/')
def index():
    error = request.args.get('error')
    return render_template('index.html', error=error)

@app.route('/request', methods=['POST'])
def make_request():
    try:
        sender_email = '1221107320@student.mmu.edu.my'
        sender_password = "R@ziq123"
        gmail = request.form.get("gmail")
        function = request.form.get("function")
        symbol = request.form.get("symbol")
        interval = request.form.get("interval")
        url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&apikey={API_KEY}'
        response = requests.get(url) 
        msg = MIMEMultipart('alternative')
        subject = f"You added {function} , {symbol} , {interval}"
        msg['FROM'] = sender_email
        msg['TO'] = gmail
        msg['SUBJECT'] = subject
        smtp_server = 'smtp-mail.outlook.com'
        smtp_port = 587

        try:
            # create a secured SSl/TLS Connection
            server = smtplib.SMTP(smtp_server , smtp_port)
            server.starttls()

            server.login(sender_email , sender_password)
            server.sendmail(sender_email , gmail , msg.as_string())
            print('Email sent successfully')

        except smtplib.SMTPException as e:
            print("error sending email" , str(e))

        finally:
            server.quit()
        data = response.json()
        if data.get('Error Message'):
            return redirect(url_for('index', error=data.get('Error Message')))
        return redirect(url_for('result', data=json.dumps(data)))
    except Exception as e:
        return str(e)
    
@app.route('/result')
def result():
    data = request.args.get('data')
    if data:
        data = json.loads(data)  # Parse the JSON string into a dictionary
    simplified_data = f.simplify_data(data)
    return render_template('results.html', data=simplified_data)
        
@app.route('/reactTest')
def reactTest():
    return jsonify(message= 'Hello from Flask!')

if __name__ == '__main__':
    app.run(debug=True)