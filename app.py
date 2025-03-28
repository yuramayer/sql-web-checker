"""Flask App Web Page Module"""

from flask import Flask, render_template, request
from processing import check_code

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Main App Page"""
    if request.method == 'POST':

        text = request.form['text']

        df = check_code(text)

        result_html = df.to_html(classes='table table-striped', index=False)

        return render_template('index.html', result=result_html)

    return render_template('index.html', result=None)


if __name__ == '__main__':
    app.run(debug=True)
