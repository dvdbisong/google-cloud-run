import os
import pandas as pd
import pandas_profiling

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    return 'Hello {}!\n'.format(target)

@app.route('/profile')
def profile():
    # importing the data
    df = pd.read_csv(request.args.get('data'))
    profile = pandas_profiling.ProfileReport(df)
    profile.to_file(output_file="templates/output.html")
    return render_template('output.html')

@app.route('/query-example')
def query_example():
    language = request.args.get('language') #if key doesn't exist, returns None

    return '''<h1>The language value is: {}</h1>'''.format(language)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))