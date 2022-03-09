#!/bin/python3

from flask import Flask, jsonify
app = Flask(__name__)
import subprocess
import datetime

@app.route('/')
def env_greet():
    env_info_raw = subprocess.getoutput('/usr/bin/python3 env_data_getter.py')
    temp, press, humid = map(float, env_info_raw.split('\n'))
    dt_now = datetime.datetime.now()
    timestamp = dt_now.strftime('%Y-%m-%d-%H-%M-%S')

    env_dict = {'timestamp': timestamp, 'temp': temp, 'press': press, 'humid': humid}
    return jsonify(env_dict)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
