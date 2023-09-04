from flask import Flask, request, jsonify
import pandas as pd
from api import static

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to alice land</h1>"

@app.route('/static/')
def static_info():
    this_static = static()
    events = this_static.get_events()
    return events.to_json(orient="records")

if __name__ == '__main__':
    app.run(debug=True)