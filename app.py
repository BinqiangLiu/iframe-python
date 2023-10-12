from flask import Flask, send_file
import os
from dotenv import load_dotenv

load_dotenv()
port = os.getenv('port')

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('templates/index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
