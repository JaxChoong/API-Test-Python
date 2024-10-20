from flask import Flask, request, jsonify,render_template,redirect,url_for
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

API_KEY = os.getenv('API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/request', methods=['POST'])
def make_request():
    try:
        function = request.form.get("function")
        symbol = request.form.get("symbol")
        interval = request.form.get("interval")
        url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&apikey={API_KEY}'
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return str(e)
        

if __name__ == '__main__':
    app.run(debug=True)