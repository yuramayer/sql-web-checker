"""Flask App Web Page Module"""

from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Main App Page"""
    if request.method == 'POST':
        # text = request.form['text']

        df = pd.DataFrame([[1, 2, 3], ['a', 'b', 'c']], columns=[1, 2, 3])

        result_html = df.to_html(classes='table table-striped', index=False)

        return render_template('index.html', result=result_html)

    return render_template('index.html', result=None)


if __name__ == '__main__':
    app.run(debug=True)
