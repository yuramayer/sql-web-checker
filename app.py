"""Flask App Web Page Module"""

from flask import Flask, Response, request, send_from_directory
from processing import check_code

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Main App Page"""

    table_html = '<p style="color:red;"Введи SQL-код для обработки</p>'

    if request.method == 'POST':

        text_input = request.form.get('text_input', '')

        if text_input:
            try:
                df = check_code(text_input)
                if df.empty:
                    table_html = '<p style="color:green;">В \
                        коде нет простых ошибок :)</p>'
                else:
                    table_html = df.to_html(
                        index=False, classes='errors_table', escape=False)
            except Exception as err:  # pylint: disable=broad-except

                table_html = f'<p style="color:red;">\
                    Ошибка обработки кода: {err}</p>'

    with open('index.html', 'r', encoding='utf-8') as webpage:
        html_content = webpage.read()

    html_content = html_content.replace('<!-- TABLE -->', table_html)

    return Response(html_content, mimetype='text/html')


@app.route('/static/<path:filename>')
def static_files(filename):
    """Add css to the flask web app"""
    return send_from_directory('static', filename)


if __name__ == '__main__':
    app.run(debug=True)
