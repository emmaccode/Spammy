import flask
import json
from flask import Flask, render_template, request
from joblib import load
import pandas as pd
# <--- Deps --->
# (Main)
app = Flask(__name__)
if __name__ == '__main__':
    app.run()

@app.route('/')
def template():
    try:
        txt = request.args['text']
    except KeyError as e:
        return ('Some Values are missing')
    df = pd.DataFrame({'input': [txt]})
    pipeline = load('alg.sav')
    estimate = pipeline.predict(df['input'])
    return(estimate)

if __name__ == '__main__':
    app.run(debug=False)
