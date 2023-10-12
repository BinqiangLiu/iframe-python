from flask import Flask, render_template
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
import os
from dotenv import load_dotenv
load_dotenv()
port=os.getenv('port')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')    

if __name__ == '__main__':
   # app.run()
    app.run(host='0.0.0.0', port=port)
