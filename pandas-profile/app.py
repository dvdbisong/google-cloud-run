import os
import pandas as pd
import pandas_profiling

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile')
def profile():
    # importing the data
    df = pd.read_csv(request.args.get('data'))
    profile = pandas_profiling.ProfileReport(df)
    profile.to_file(output_file="templates/output.html")
    return render_template('output.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))