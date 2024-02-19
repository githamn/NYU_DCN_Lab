from flask import Flask
import datetime
import time

app = Flask(__name__)
now = datetime.datetime.now()

@app.route('/')
def Welcome():
    return 'ZW4074'

@app.route('/time')
def print_current_time():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return "Current Time: " + current_time

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
