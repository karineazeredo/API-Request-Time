from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route('/time', methods=['GET'])
def home():
    return jsonify(datetime.now().strftime("%H:%M:%S"))


app.run()