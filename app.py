from flask import Flask
from flask import request
from flask import jsonify

import requests

import os

app = Flask(__name__)

verificiation_token=os.environ['VERIFICATION_TOKEN']

@app.route('/')
def hello():
    return "Earth Sci Weather for Slack"

@app.route('/earthsci', methods=['POST'])
def earthsci():
    # do the thing
    # grab the data
    if request.form['token'] == verification_token:
        q = requests.get('http://128.250.56.142:8000/current-weather/').json()

        ret_str = 'The current temperature is %0.1f degrees, with a humidity of %0.1f%% with a wind speed of %0.1f kph.' % (q['curr_temp'], q['curr_humid'], q['curr_wind_spd'])
        ret = {'text': ret_str}

        return jsonify(ret)

if __name__ == '__main__':
    app.run()
